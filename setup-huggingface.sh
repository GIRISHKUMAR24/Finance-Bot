#!/bin/bash

# Hugging Face Setup Script for Finance Bot
echo "🤖 Setting up Hugging Face integration for Finance Bot..."

# Navigate to project directory
cd "$(dirname "$0")"

# Install Hugging Face packages
echo "📦 Installing Hugging Face packages..."
npm install @huggingface/inference

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "✅ Hugging Face packages installed successfully!"
else
    echo "❌ Failed to install packages. Please try running 'npm install @huggingface/inference' manually."
    exit 1
fi

# Check if .env file exists
if [ -f ".env" ]; then
    # Check if HF API key is configured
    if grep -q "VITE_HUGGINGFACE_API_KEY=your-huggingface-api-key-here" .env; then
        echo ""
        echo "⚠️  IMPORTANT: Please configure your Hugging Face API key"
        echo "1. Visit https://huggingface.co/settings/tokens"
        echo "2. Create a new access token"
        echo "3. Replace 'your-huggingface-api-key-here' in .env file with your actual key"
        echo ""
        echo "Example:"
        echo "VITE_HUGGINGFACE_API_KEY=hf_your_actual_api_key_here"
    else
        echo "✅ Hugging Face API key appears to be configured"
    fi
else
    echo "❌ .env file not found. Please create one with your Hugging Face API key."
    exit 1
fi

echo ""
echo "🚀 Setup complete! You can now:"
echo "1. Run 'npm start' to start the development server"
echo "2. Visit the dashboard to see AI insights"
echo "3. Try the AI chat interface"
echo "4. Test auto-categorization when adding expenses"
echo ""
echo "📖 For detailed setup instructions, see HUGGING_FACE_SETUP.md"
