# 🤖 Finance Bot - Complete Setup Guide

## 🔧 Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed  
- Hugging Face account and API key

## 📝 API Key Setup

### 1. Get Your Hugging Face API Key
1. Visit [Hugging Face](https://huggingface.co/settings/tokens)
2. Create a new token with "Read" permissions
3. Copy the token (starts with `hf_`)

### 2. Update Environment Variables
Open `.env` file and replace:
```bash
# For React app
VITE_HUGGINGFACE_API_KEY=hf_your_actual_token_here

# For Streamlit app  
HUGGINGFACE_API_KEY=hf_your_actual_token_here
```

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Run the setup script
./setup-huggingface.bat

# Start both applications
./start-both.bat
```

### Option 2: Manual Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install

# Start Streamlit (Terminal 1)
streamlit run streamlit_app.py

# Start React app (Terminal 2)
npm start
```

## 🌐 Access Your Applications

### Streamlit Finance Bot
- **URL:** http://localhost:8501
- **Features:** 
  - AI-powered financial advice
  - Expense tracking and analysis
  - Interactive charts and insights
  - Hugging Face integration for smart categorization

### React Finance Bot  
- **Development:** http://localhost:4028
- **Production Build:** Use `npm run build` then deploy `/build` folder
- **Features:**
  - Modern React interface
  - AI chat integration
  - Real-time financial dashboards
  - Mobile-responsive design

## 🔧 Troubleshooting

### Hugging Face Issues
1. **API Key Error:** Ensure your `.env` file has the correct API key
2. **Model Loading:** Some models may take 20+ seconds to load initially
3. **Rate Limits:** Free tier has usage limits

### Port Conflicts
- **Streamlit (8501):** Change in `.streamlit/config.toml`
- **React (4028):** Change in `vite.config.mjs`

### Build Issues
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Clear Python cache
pip cache purge
```

## 📦 Dependencies Overview

### Python (Streamlit)
- `streamlit` - Web app framework
- `transformers` - Hugging Face models
- `plotly` - Interactive charts
- `pandas` - Data manipulation

### JavaScript (React)
- `@huggingface/inference` - API client
- `react` - UI framework  
- `vite` - Build tool
- `tailwindcss` - Styling

## 🎯 Next Steps
1. Customize AI models in `huggingface_service.py`
2. Add your own financial data
3. Deploy to production (Streamlit Cloud, Vercel, etc.)
4. Explore additional Hugging Face models

## 📚 Documentation
- [Hugging Face Docs](https://huggingface.co/docs)
- [Streamlit Docs](https://docs.streamlit.io)
- [React Docs](https://react.dev)
