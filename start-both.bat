@echo off
echo 🚀 Starting Finance Bot Application...
echo.

REM Check if ports are available
netstat -an | findstr :8501 >nul
if %ERRORLEVEL% equ 0 (
    echo ⚠️ Port 8501 is already in use. Streamlit might already be running.
    echo.
)

netstat -an | findstr :4028 >nul
if %ERRORLEVEL% equ 0 (
    echo ⚠️ Port 4028 is already in use. React dev server might already be running.
    echo.
)

echo Starting services...
echo.

REM Start Streamlit in background
echo 📊 Starting Streamlit Finance Bot...
start "Streamlit Finance Bot" cmd /k "streamlit run streamlit_app.py"

REM Wait a moment for Streamlit to start
timeout /t 3 /nobreak >nul

REM Start React development server
echo ⚛️ Starting React Development Server...
start "React Finance Bot" cmd /k "npm start"

echo.
echo 🎉 Both services are starting!
echo.
echo 📊 Streamlit App: http://localhost:8501
echo ⚛️ React App: http://localhost:4028
echo.
echo Press any key to exit...
pause >nul
