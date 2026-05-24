@echo off
cd /d "%~dp0.."
git add .
git commit -m "feat: posts 01-15 con imagenes"
git push origin main
pause
