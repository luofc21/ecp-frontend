# push-to-github.ps1
# GitHub 仓库推送脚本

$ErrorActionPreference = "Stop"

# 颜色定义
function Write-Step { param($msg) Write-Host "[步骤] $msg" -ForegroundColor Yellow }
function Write-Success { param($msg) Write-Host "[成功] $msg" -ForegroundColor Green }
function Write-Info { param($msg) Write-Host "[信息] $msg" -ForegroundColor Cyan }
function Write-Err { param($msg) Write-Host "[错误] $msg" -ForegroundColor Red }

Write-Host "==========================================" -ForegroundColor Magenta
Write-Host "   GitHub 仓库推送脚本" -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host ""

# 检查 Git
try {
    $gitVersion = git --version 2>$null
    if (-not $gitVersion) { throw "Git not found" }
    Write-Info "Git 已安装: $gitVersion"
} catch {
    Write-Err "Git 未安装，请先安装 Git"
    Read-Host "按 Enter 退出"
    exit 1
}

# 检查 curl
try {
    $curlVersion = curl --version 2>$null
    if (-not $curlVersion) { throw "curl not found" }
    Write-Info "curl 已安装"
} catch {
    Write-Err "curl 未安装，请先安装 curl"
    Read-Host "按 Enter 退出"
    exit 1
}

# 交互式输入
Write-Host ""
Write-Host "请输入 GitHub 用户名:" -NoNewline
$USERNAME = Read-Host

Write-Host "请输入仓库名称:" -NoNewline
$REPO_NAME = Read-Host

Write-Host "请输入 Access Token:" -NoNewline
$TOKEN = Read-Host

Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host "用户名: $USERNAME"
Write-Host "仓库名: $REPO_NAME"
Write-Host "Token:  ****（已隐藏）"
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host ""

# 验证输入
if ([string]::IsNullOrWhiteSpace($USERNAME)) {
    Write-Err "用户名不能为空"
    exit 1
}
if ([string]::IsNullOrWhiteSpace($REPO_NAME)) {
    Write-Err "仓库名不能为空"
    exit 1
}
if ([string]::IsNullOrWhiteSpace($TOKEN)) {
    Write-Err "Token 不能为空"
    exit 1
}

# ========== 1. 初始化 Git 仓库 ==========
if (-not (Test-Path ".git")) {
    Write-Step "初始化 Git 仓库..."
    git init
    git config init.defaultBranch main
    Write-Success "Git 仓库初始化完成"
} else {
    Write-Info "Git 仓库已存在，跳过初始化"
}

# 配置用户信息
if (-not (git config user.name)) {
    git config user.name $USERNAME
}
if (-not (git config user.email)) {
    git config user.email "$USERNAME@users.noreply.github.com"
}

# ========== 2. 创建远程仓库 ==========
Write-Step "创建远程仓库 ${USERNAME}/${REPO_NAME}..."

$body = @{
    name        = $REPO_NAME
    private     = $true
    description = "$REPO_NAME project"
} | ConvertTo-Json

$headers = @{
    "Authorization" = "Bearer $TOKEN"
    "Content-Type"  = "application/json"
}

try {
    $response = Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Method Post -Headers $headers -Body $body -ErrorAction Stop
    Write-Success "远程仓库创建成功"
    $repoCreated = $true
} catch {
    # 可能已存在，检查是否是 422 错误（仓库已存在）
    $errorMsg = $_.Exception.Message
    if ($errorMsg -match "already exists") {
        Write-Info "远程仓库已存在，继续操作"
        $repoCreated = $false
    } else {
        Write-Err "创建仓库失败: $errorMsg"
        Read-Host "按 Enter 退出"
        exit 1
    }
}

# ========== 3. 配置远程仓库 ==========
Write-Step "配置远程仓库..."
git remote remove origin 2>$null
git remote add origin "https://${TOKEN}@github.com/${USERNAME}/${REPO_NAME}.git"
Write-Success "远程仓库配置完成"

# ========== 4. 创建 .gitignore ==========
if (-not (Test-Path ".gitignore")) {
    Write-Step "创建 .gitignore..."
    @"
*.zip
*.pyc
__pycache__/
.env
.DS_Store
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Success ".gitignore 已创建"
} else {
    Write-Info ".gitignore 已存在，跳过"
}

# ========== 5. 检查并处理大文件 ==========
Write-Step "检查大文件..."

$LFSInstalled = $true
try {
    git lfs version 2>$null | Out-Null
} catch {
    $LFSInstalled = $false
}

# 查找超过 50MB 的文件
$largeFiles = Get-ChildItem -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 50MB -and $_.FullName -notmatch "\.git" }

if ($largeFiles) {
    Write-Info "发现以下大文件 (>50MB):"
    $largeFiles | ForEach-Object { Write-Host "  - $($_.FullName) ($([math]::Round($_.Length / 1MB, 2)) MB)" }

    if ($LFSInstalled) {
        Write-Info "使用 Git LFS 管理大文件..."

        # 初始化 LFS
        git lfs install 2>$null | Out-Null

        # 追踪大文件扩展名
        $extensions = $largeFiles | ForEach-Object { $_.Extension } | Select-Object -Unique
        foreach ($ext in $extensions) {
            if ($ext) {
                Write-Host "  追踪: $ext" -ForegroundColor Gray
                git lfs track $ext 2>$null
            }
        }

        # 提交 .gitattributes
        if (Test-Path ".gitattributes") {
            git add .gitattributes
            git commit -m "chore: add .gitattributes for LFS" 2>$null
        }

        # 迁移到 LFS
        Write-Info "迁移大文件到 LFS..."
        $includePatterns = $extensions | Where-Object { $_ } | ForEach-Object { "*$_" }
        $includeArg = $includePatterns -join ","
        git lfs migrate import --everything --include=$includeArg --yes 2>$null
        Write-Success "LFS 迁移完成"
    } else {
        Write-Warn "Git LFS 未安装，大文件将直接推送（可能触发 GitHub 警告）"
    }
} else {
    Write-Info "无超过 50MB 的大文件"
}

# ========== 6. 提交文件 ==========
Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Step "提交文件到本地仓库..."
git add -A
$commit = git commit -m "Initial commit" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Success "提交成功"
} else {
    Write-Info "没有需要提交的文件或已是最新"
}

# ========== 7. 推送到远程 ==========
Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Step "推送到远程仓库..."
git push -u origin main --force
if ($LASTEXITCODE -eq 0) {
    Write-Success "推送成功"
} else {
    Write-Err "推送失败"
    Read-Host "按 Enter 退出"
    exit 1
}

# ========== 完成 ==========
Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host "   推送完成!" -ForegroundColor Green
Write-Host "   仓库地址: https://github.com/$USERNAME/$REPO_NAME" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Magenta
Read-Host "按 Enter 退出"
