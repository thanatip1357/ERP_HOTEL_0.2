@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

REM Run Odoo with the correct configuration file path
python odoo-bin -c debian\odoo.conf

REM Pause (optional: keeps the terminal open if there are errors)
pause
