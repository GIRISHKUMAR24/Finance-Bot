@echo off
echo 🤖 Setting up Hugging Face integration for Finance Bot...
echo.

REM Navigate to project directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org
    pause
    exit /b 1
)

REM Install Python dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Error: Failed to install Python dependencies
    pause
    exit /b 1
)

REM Install Hugging Face packages
echo 📦 Installing Hugging Face packages...
call npm install @huggingface/inference

REM Check if installation was successful
if %ERRORLEVEL% equ 0 (
    echo ✅ Hugging Face packages installed successfully!
) else (
    echo ❌ Failed to install packages. Please try running 'npm install @huggingface/inference' manually.
    pause
    exit /b 1
)

REM Check if .env file exists
if exist ".env" (
    REM Check if HF API key is configured
    findstr /c:"VITE_HUGGINGFACE_API_KEY=your-huggingface-api-key-here" .env >nul
    if %ERRORLEVEL% equ 0 (
        echo.
        echo ⚠️  IMPORTANT: Please configure your Hugging Face API key
        echo 1. Visit https://huggingface.co/settings/tokens
        echo 2. Create a new access token
        echo 3. Replace 'your-huggingface-api-key-here' in .env file with your actual key
        echo.
        echo Example:
        echo VITE_HUGGINGFACE_API_KEY=hf_your_actual_api_key_here
    ) else (
        echo ✅ Hugging Face API key appears to be configured
    )
) else (
    echo ❌ .env file not found. Please create one with your Hugging Face API key.
    pause
    exit /b 1
)

echo.
echo 🚀 Setup complete! You can now:
echo 1. Run 'npm start' to start the development server
echo 2. Visit the dashboard to see AI insights
echo 3. Try the AI chat interface
echo 4. Test auto-categorization when adding expenses
echo.
echo 📖 For detailed setup instructions, see HUGGING_FACE_SETUP.md
echo.
pause
