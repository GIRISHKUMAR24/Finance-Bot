# Finance Bot - AI-Powered Financial Assistant

A comprehensive financial management application built with Streamlit and powered by Hugging Face AI models.

## 🚀 Features

- **AI Financial Advice** - Get personalized financial recommendations using Hugging Face models
- **Expense Tracking** - Track and categorize your expenses with smart AI categorization
- **Interactive Dashboards** - Visualize your financial data with interactive charts
- **Financial Goals** - Set and track your financial goals with AI insights
- **Sentiment Analysis** - Analyze the sentiment of your financial decisions
- **Smart Insights** - Receive AI-powered insights about your spending patterns

## 📋 Prerequisites

- Python 3.8 or higher
- Hugging Face API key (free at https://huggingface.co)

## 🛠️ Quick Start

### Option 1: Simple Run (Recommended)
```bash
# Just run this command:
./run.bat                    # Windows
# or
streamlit run streamlit_app.py
```

### Option 2: Detailed Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment (optional for AI features)
cp .env.template .env
# Edit .env with your Hugging Face API key

# Run the application  
streamlit run streamlit_app.py
```

## 🔧 Configuration

### Get Hugging Face API Key (Optional)
1. Visit [Hugging Face](https://huggingface.co/settings/tokens)
2. Create a free account
3. Generate a new token with "Read" permissions
4. Copy `.env.template` to `.env`
5. Replace `your-huggingface-api-key-here` with your actual key

### App Access
- **Streamlit App:** http://localhost:8501
- **AI Features:** Enabled with API key, works without it too

## 📁 Project Structure

```
├── streamlit_app.py           # Main Streamlit application
├── huggingface_service.py     # AI integration service
├── requirements.txt           # Python dependencies
├── .env.template             # Environment configuration template
├── run.bat                   # Quick start script
├── README_STREAMLIT.md       # Detailed Streamlit guide
└── src/                      # React components (optional)
```

## 🚀 Features Overview

### 📊 **Dashboard**
- Financial overview with AI insights
- Recent transactions analysis
- Goal progress tracking
- Spending pattern visualization

### 💰 **Expense Management**
- Add/edit expenses with smart categorization
- AI-powered expense analysis
- Category-wise spending breakdown
- Export functionality

### 🎯 **Financial Goals**
- Set and track financial objectives
- AI recommendations for goal achievement
- Progress visualization
- Smart milestone tracking

### 🤖 **AI Assistant**
- Natural language financial queries
- Personalized advice and recommendations
- Sentiment analysis of financial decisions
- Smart insights and predictions

## 🛠️ Development

### React Frontend (Optional)
```bash
npm install              # Install dependencies
npm start               # Development server (port 4028)
npm run build           # Production build
```

### Python Backend
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🔄 Deployment

### Streamlit Cloud
1. Push to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy directly from repository

### Local Deployment
```bash
# Just run the app
streamlit run streamlit_app.py
```

## 🎯 Usage Tips

1. **Without API Key:** App works with demo data and basic features
2. **With API Key:** Full AI capabilities including chat and smart insights
3. **Data Privacy:** All data stays local, only AI queries sent to Hugging Face
4. **Performance:** First AI request may take 20-30 seconds (model loading)

## 🆘 Troubleshooting

### Common Issues
- **Port 8501 in use:** Close existing Streamlit apps or change port
- **Missing dependencies:** Run `pip install -r requirements.txt`
- **API errors:** Check your `.env` file and API key validity

### Getting Help
- Check `README_STREAMLIT.md` for detailed Streamlit guide
- Review `SETUP_GUIDE.md` for comprehensive setup instructions
- Open an issue on GitHub for technical problems

## 🎉 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ using Streamlit and Hugging Face AI**
   
2. Start the development server:
   ```bash
   npm start
   # or
   yarn start
   ```

## 📁 Project Structure

```
react_app/
├── public/             # Static assets
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/          # Page components
│   ├── styles/         # Global styles and Tailwind configuration
│   ├── App.jsx         # Main application component
│   ├── Routes.jsx      # Application routes
│   └── index.jsx       # Application entry point
├── .env                # Environment variables
├── index.html          # HTML template
├── package.json        # Project dependencies and scripts
├── tailwind.config.js  # Tailwind CSS configuration
└── vite.config.js      # Vite configuration
```

## 🧩 Adding Routes

To add new routes to the application, update the `Routes.jsx` file:

```jsx
import { useRoutes } from "react-router-dom";
import HomePage from "pages/HomePage";
import AboutPage from "pages/AboutPage";

const ProjectRoutes = () => {
  let element = useRoutes([
    { path: "/", element: <HomePage /> },
    { path: "/about", element: <AboutPage /> },
    // Add more routes as needed
  ]);

  return element;
};
```

## 🎨 Styling

This project uses Tailwind CSS for styling. The configuration includes:

- Forms plugin for form styling
- Typography plugin for text styling
- Aspect ratio plugin for responsive elements
- Container queries for component-specific responsive design
- Fluid typography for responsive text
- Animation utilities

## 📱 Responsive Design

The app is built with responsive design using Tailwind CSS breakpoints.


## 📦 Deployment

Build the application for production:

```bash
npm run build
```

## 🙏 Acknowledgments

- Built with [Rocket.new](https://rocket.new)
- Powered by React and Vite
- Styled with Tailwind CSS

Built with ❤️ on Rocket.new
