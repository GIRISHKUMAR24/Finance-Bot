# 🤖 Finance Bot - Streamlit Edition

## 🎯 Quick Start

### Super Simple Setup:
```bash
# Just double-click this file:
run.bat

# Or run in terminal:
streamlit run streamlit_app.py
```

### Your app will open at: http://localhost:8501

## 🔧 First Time Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Hugging Face API Key (Optional)
1. Get free API key from: https://huggingface.co/settings/tokens
2. Edit `.env` file:
   ```
   HUGGINGFACE_API_KEY=hf_your_actual_token_here
   ```

## 🌟 What You Get

### ✅ **Complete Finance Management**
- 📊 Expense tracking and analysis
- 🎯 Financial goal setting
- 📈 Interactive charts and visualizations
- 💡 AI-powered insights (with Hugging Face)

### ✅ **AI Features (with API key)**
- 🤖 Smart expense categorization
- 💬 Financial advice chatbot
- 📊 Sentiment analysis of spending
- 🎯 Personalized recommendations

### ✅ **Works Without API Key**
- All core features work
- Demo data and examples included
- Local calculations and insights

## 🚀 Running the App

### Method 1: Double-click
- `run.bat` - Simplest way

### Method 2: Command Line
```bash
streamlit run streamlit_app.py
```

### Method 3: Detailed Setup
```bash
start-streamlit.bat
```

## 🔄 App Features

### 📊 **Dashboard**
- Financial overview
- Recent transactions
- Goal progress
- AI insights

### 💰 **Expense Tracking**
- Add/edit expenses
- Category management
- Spending analysis
- Export data

### 🎯 **Goals**
- Set financial goals
- Track progress
- Get recommendations
- Visual progress

### 🤖 **AI Chat** (requires API key)
- Ask financial questions
- Get personalized advice
- Smart insights

## 🛠️ Troubleshooting

### Port Already in Use?
```bash
# Kill existing process
taskkill /f /im python.exe

# Then restart
streamlit run streamlit_app.py
```

### Missing Dependencies?
```bash
pip install -r requirements.txt
```

### API Not Working?
- App works without API key
- Check your `.env` file
- Verify API key is valid

## 📁 Project Structure
```
├── streamlit_app.py        # Main application
├── huggingface_service.py  # AI integration
├── requirements.txt        # Dependencies
├── .env                   # Configuration
├── run.bat               # Quick start
└── README_STREAMLIT.md   # This guide
```

## 🎉 Enjoy Your Finance Bot!

Your AI-powered financial assistant is ready to help you manage your money smarter! 💰✨
