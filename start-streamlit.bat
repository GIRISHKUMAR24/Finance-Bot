@echo off
echo 🚀 Starting Finance Bot with Streamlit...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if Streamlit is installed
pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing Streamlit and dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Check if port 8501 is available
netstat -an | findstr :8501 >nul
if %ERRORLEVEL% equ 0 (
    echo ⚠️ Port 8501 is already in use. 
    echo A Streamlit app might already be running.
    echo.
    choice /c YN /m "Do you want to continue anyway"
    if errorlevel 2 exit /b 0
    echo.
)

echo 📊 Starting Streamlit Finance Bot...
echo.
echo 🌐 The app will open in your browser at: http://localhost:8501
echo 🔧 To stop the app, press Ctrl+C in this window
echo.

REM Start Streamlit
streamlit run streamlit_app.py

echo.
echo Finance Bot stopped.
pause
