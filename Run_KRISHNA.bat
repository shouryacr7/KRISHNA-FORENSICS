@echo off
TITLE KRISHNA Framework - @thesudosiuu
color 0b

:: Folder path set karna
cd /d "%~dp0"

:: Admin Check
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] ERROR: Please Right-Click and 'Run as Administrator'.
    pause
    exit /b
)

echo [*] Initializing KRISHNA...

:: Requirements check
python -m pip install psutil colorama --quiet

echo [*] Launching Framework...
echo.

:: Python script ko execute karega
python KRISHNA.py

echo.
echo ============================================================
echo [✓] KRISHNA Scan Finished.
echo [!] Returning to Normal Terminal Mode...
echo ============================================================
echo.

:: YE HAI MAGIC LINE: Isse CMD band nahi hoga
cmd /k