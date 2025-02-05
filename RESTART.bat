@echo off
echo Stopping Odoo Server...

:: Kill any running Python processes (force stop Odoo)
taskkill /F /IM python.exe >nul 2>&1

echo Restarting Odoo...
timeout /t 3 /nobreak >nul

:: Start the main Odoo run script
start cmd /k "cd /d C:\Users\LENOVO\Desktop\Work\PROJECT\The_ERP\ERP_HOTEL_0.2 && call RUN_ME.bat"
exit
