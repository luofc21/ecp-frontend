@echo off
chcp 65001 >nul
echo ==========================================
echo    GitHub 仓库推送脚本
echo ==========================================
echo.
echo 正在启动 PowerShell 脚本...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0push-to-github.ps1"
pause
