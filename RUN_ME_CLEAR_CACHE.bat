@echo off
title Odoo 16 Server - Hotel ERP

REM Activate virtual environment
call .venv\Scripts\activate

REM Upgrade ALL modules and stop
echo Updating all Odoo modules...
python odoo-bin -c debian\odoo.conf --update=all --stop-after-init

REM Clear Odoo cache
echo Clearing Odoo cache...
rmdir /s /q "C:\Users\LENOVO\AppData\Local\openerp s.a\odoo"

REM Start Odoo Server
echo Starting Odoo Server...
python odoo-bin -c debian\odoo.conf

REM Keep CMD open
pause
