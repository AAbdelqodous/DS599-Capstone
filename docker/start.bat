@echo off
cd /d "%~dp0"
docker compose up -d --build
echo.
echo Jupyter is starting. Open http://localhost:8888 in your browser.
timeout /t 5 >nul
start http://localhost:8888
pause
