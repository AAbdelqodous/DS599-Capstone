@echo off
cd /d "%~dp0"
docker compose down
echo Stopped. Your files are still in the work folder.
pause
