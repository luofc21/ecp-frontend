#!/bin/bash
# push-to-github.sh
# 初始化本地 Git 项目并推送到 GitHub，支持大文件 LFS 管理

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

echo -e "${MAGENTA}==========================================${NC}"
echo -e "${MAGENTA}   GitHub 仓库推送脚本${NC}"
echo -e "${MAGENTA}==========================================${NC}"
echo ""

# 检测 Git 是否安装
if ! command -v git &> /dev/null; then
    echo -e "${RED}[错误] Git 未安装，请先安装 Git${NC}"
    exit 1
fi
echo -e "${CYAN}[信息] Git 已安装: $(git --version)${NC}"

# 检测 curl 是否安装
if ! command -v curl &> /dev/null; then
    echo -e "${RED}[错误] curl 未安装，请先安装 curl${NC}"
    exit 1
fi
echo -e "${CYAN}[信息] curl 已安装${NC}"

# 检测 Git LFS 是否安装
LFS_INSTALLED=false
if command -v git-lfs &> /dev/null; then
    LFS_INSTALLED=true
    git lfs install --quiet 2>/dev/null || true
    echo -e "${CYAN}[信息] Git LFS 已安装${NC}"
else
    echo -e "${YELLOW}[警告] Git LFS 未安装，大文件将直接推送${NC}"
fi

# 交互式输入
echo ""
echo "请输入 GitHub 用户名:"
read -r USERNAME

echo "请输入仓库名称:"
read -r REPO_NAME

echo "请输入 Access Token (输入时不可见):"
read -r -s TOKEN

echo ""
echo -e "${MAGENTA}==========================================${NC}"
echo -e "用户名: ${USERNAME}"
echo -e "仓库名: ${REPO_NAME}"
echo -e "Token:  ****（已隐藏）"
echo -e "${MAGENTA}==========================================${NC}"
echo ""

# 验证输入
if [[ -z "$USERNAME" || -z "$REPO_NAME" || -z "$TOKEN" ]]; then
    echo -e "${RED}[错误] 用户名、仓库名和 Token 不能为空${NC}"
    exit 1
fi

REMOTE_URL="https://${TOKEN}@github.com/${USERNAME}/${REPO_NAME}.git"

# ========== 1. 初始化 Git 仓库 ==========
echo -e "${YELLOW}[步骤 1/6] 初始化 Git 仓库...${NC}"
if [ ! -d ".git" ]; then
    git init
    git config init.defaultBranch main
    echo -e "${GREEN}[成功] Git 仓库初始化完成${NC}"
else
    echo -e "${CYAN}[信息] Git 仓库已存在，跳过初始化${NC}"
fi

# 设置用户信息（如果未设置）
if [ -z "$(git config user.name)" ]; then
    git config user.name "${USERNAME}"
fi
if [ -z "$(git config user.email)" ]; then
    git config user.email "${USERNAME}@users.noreply.github.com"
fi

# ========== 2. 创建远程仓库 ==========
echo -e "${YELLOW}[步骤 2/6] 创建远程仓库 ${USERNAME}/${REPO_NAME}...${NC}"

# 检查仓库是否已存在
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "https://api.github.com/repos/${USERNAME}/${REPO_NAME}" \
    -H "Authorization: Bearer ${TOKEN}")

if [ "$HTTP_CODE" == "200" ]; then
    echo -e "${CYAN}[提示] 远程仓库已存在，继续操作${NC}"
    REPO_EXISTS=true
elif [ "$HTTP_CODE" == "404" ]; then
    # 仓库不存在，创建它
    API_RESPONSE=$(curl -s -X POST "https://api.github.com/user/repos" \
        -H "Authorization: Bearer ${TOKEN}" \
        -H "Content-Type: application/json" \
        -d "{\"name\":\"${REPO_NAME}\",\"private\":true,\"description\":\"${REPO_NAME} project\"}")

    if echo "$API_RESPONSE" | grep -q '"id"'; then
        echo -e "${GREEN}[成功] 远程仓库创建成功${NC}"
        REPO_EXISTS=false
    else
        ERROR_MSG=$(echo "$API_RESPONSE" | grep -o '"message":"[^"]*"' | head -1)
        echo -e "${RED}[错误] 创建仓库失败: ${ERROR_MSG}${NC}"
        exit 1
    fi
else
    echo -e "${RED}[错误] 检查仓库失败，HTTP 状态码: ${HTTP_CODE}${NC}"
    exit 1
fi

# ========== 3. 配置远程仓库 ==========
echo -e "${YELLOW}[步骤 3/6] 配置远程仓库...${NC}"
git remote remove origin 2>/dev/null || true
git remote add origin "${REMOTE_URL}"
echo -e "${GREEN}[成功] 远程仓库配置完成${NC}"

# ========== 4. 创建 .gitignore ==========
echo -e "${YELLOW}[步骤 4/6] 创建 .gitignore...${NC}"
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOF'
*.zip
*.pyc
__pycache__/
.env
.DS_Store
EOF
    echo -e "${GREEN}[成功] .gitignore 已创建${NC}"
else
    echo -e "${CYAN}[提示] .gitignore 已存在，跳过创建${NC}"
fi

# ========== 5. 检查并处理大文件 ==========
echo -e "${YELLOW}[步骤 5/6] 检查大文件...${NC}"

# 查找所有超过 50MB 的大文件（排除 .git 目录）
LARGE_FILES=$(find . -type f -size +50M -not -path "./.git/*" 2>/dev/null || true)

if [ -n "$LARGE_FILES" ]; then
    echo -e "${CYAN}[检测到大文件]:${NC}"
    echo "$LARGE_FILES" | while IFS= read -r file; do
        SIZE=$(du -h "$file" | cut -f1)
        echo "  - $file ($SIZE)"
    done

    if [ "$LFS_INSTALLED" = true ]; then
        echo -e "${CYAN}[使用 Git LFS 管理大文件]${NC}"

        # 获取所有大文件的扩展名并去重
        EXTENSIONS=$(echo "$LARGE_FILES" | xargs -I{} basename {} | grep -o '\.[^.]*$' | sort -u | tr '\n' ',' | sed 's/,$//')

        # 逐个扩展名追踪
        echo "$LARGE_FILES" | xargs -I{} basename {} | grep -o '\.[^.]*$' | sort -u | while read -r ext; do
            echo "  追踪: $ext"
            git lfs track "*$ext" 2>/dev/null || true
        done

        # 添加 .gitattributes
        if [ -f ".gitattributes" ]; then
            git add .gitattributes
            git commit -m "chore: add .gitattributes for LFS" 2>/dev/null || true
        fi

        # 迁移到 LFS
        echo -e "${CYAN}[迁移大文件到 LFS...]${NC}"
        EXT_PATTERN=$(echo "$LARGE_FILES" | xargs -I{} basename {} | grep -o '\.[^.]*$' | sort -u | sed 's/^/*/' | tr '\n' ',' | sed 's/,$//')
        git lfs migrate import --everything \
            --include="*.zip,*.png,*.jpg,*.jpeg,*.pdf,*.tar,*.gz,*.tar.gz" \
            --yes 2>/dev/null
        echo -e "${GREEN}[成功] LFS 迁移完成${NC}"
    else
        echo -e "${YELLOW}[警告] Git LFS 未安装，大文件将直接推送（可能触发 GitHub 警告）${NC}"
    fi
else
    echo -e "${CYAN}[无超过 50MB 的大文件]${NC}"
fi

# ========== 6. 提交并推送 ==========
echo ""
echo -e "${MAGENTA}==========================================${NC}"
echo -e "${YELLOW}[步骤 6/6] 提交文件到本地仓库...${NC}"
git add -A
if git commit -m "Initial commit" 2>/dev/null; then
    echo -e "${GREEN}[成功] 提交完成${NC}"
else
    echo -e "${CYAN}[提示] 没有需要提交的文件或已是最新${NC}"
fi

echo ""
echo -e "${MAGENTA}==========================================${NC}"
echo -e "${YELLOW}[推送到远程仓库...]${NC}"
if git push -u origin main --force; then
    echo -e "${GREEN}[成功] 推送完成${NC}"
else
    echo -e "${RED}[错误] 推送失败${NC}"
    exit 1
fi

# ========== 完成 ==========
echo ""
echo -e "${MAGENTA}==========================================${NC}"
echo -e "${GREEN}   推送完成!${NC}"
echo -e "${CYAN}   仓库地址: https://github.com/${USERNAME}/${REPO_NAME}${NC}"
echo -e "${MAGENTA}==========================================${NC}"
