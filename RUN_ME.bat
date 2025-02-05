@echo off
title Odoo 16 Server - Hotel ERP

REM Define Variables
SET VENV_PATH=.venv\Scripts\activate
SET ODOO_BIN=python odoo-bin
SET CONFIG=debian\odoo.conf
SET MODULES=hotel_reservation
REM List modules separated by comma if multiple

REM Activate virtual environment
echo Activating virtual environment...
call %VENV_PATH%

REM Check if activation was successful
IF ERRORLEVEL 1 (
    echo Failed to activate the virtual environment.
    pause
    exit /b 1
)

REM Update Specific Modules and Stop
echo Updating module(s): %MODULES%...
%ODOO_BIN% -c %CONFIG% --update=%MODULES% --stop-after-init --logfile=odoo_update.log --dev=all

REM Check if update was successful
IF ERRORLEVEL 1 (
    echo Module update failed. Check odoo_update.log for details.
    pause
    exit /b 1
)

REM Start Odoo Server
echo Starting Odoo Server...
%ODOO_BIN% -c %CONFIG% --logfile=odoo_server.log --dev=all

REM Keep CMD open
pause
