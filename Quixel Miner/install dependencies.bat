@echo off

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and add it to your PATH.
    pause
    exit /b 1
)

:: Check if pip is installed
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

:: Install required Python libraries
echo Installing required Python libraries...
pip install requests

:: Confirmation message
echo All prerequisites have been installed.
pause
