@echo off
title MkDocs Local Preview - Legion Y9000P
chcp 65001 >nul
:: 1. 强力进入 D 盘项目根目录
cd /d "E:\my_git_ZJURay1110\workspace\note"

echo [1/3] 正在通过 Anaconda 激活 mkdocs 环境...
:: 2. 这里的路径必须指向你的 Scripts 文件夹
call "C:\Users\30664\anaconda3\Scripts\activate.bat" mkdoc

echo [2/3] 正在启动浏览器预览...
:: 3. 先打开浏览器，避免 server 运行后阻塞脚本
start http://127.0.0.1:8000

echo [3/3] 正在运行 mkdocs serve (修改 Markdown 后保存即可实时刷新)...
:: 4. 核心命令（用 python -m 避免 mkdocs.exe 启动器路径错误）
python -m mkdocs serve

pause