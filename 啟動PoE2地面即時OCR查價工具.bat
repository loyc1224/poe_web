@echo off
chcp 65001 > nul
title PoE2 地面掉落物即時 OCR 查價工具
echo 正在啟動 PoE2 地面掉落物即時 OCR 查價工具...
cd /d "%~dp0"
python -m web.drop_checker.gui_overlay
pause
