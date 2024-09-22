@echo off

:: Enable ANSI escape sequences for Windows 10 and later (to make text appear colored into the terminal)
reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f

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
