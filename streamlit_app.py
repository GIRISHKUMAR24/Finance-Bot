"""
Finance Bot - Streamlit Application
A comprehensive financial management tool with AI-powered insights using Hugging Face
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Finance Bot - AI Financial Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f2937;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #3b82f6;
    }
    .ai-insight {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .expense-card {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background: #1f2937;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = []
if 'goals' not in st.session_state:
    st.session_state.goals = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'name': 'Alex Johnson',
        'type': 'professional',
        'balance': 12450.00
    }

def main():
    # Header
    st.markdown('<h1 class="main-header">💰 Finance Bot - AI Assistant</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🚀 Navigation")
        page = st.selectbox(
            "Choose a page:",
            ["Dashboard", "AI Chat", "Expense Tracking", "Financial Goals", "Settings"]
        )
        
        st.markdown("---")
        
        # User profile
        st.subheader("👤 Profile")
        st.write(f"**Name:** {st.session_state.user_profile['name']}")
        st.write(f"**Type:** {st.session_state.user_profile['type'].title()}")
        st.write(f"**Balance:** ${st.session_state.user_profile['balance']:,.2f}")
        
        st.markdown("---")
        
        # AI Status
        hf_api_key = os.getenv('HUGGINGFACE_API_KEY')
        if hf_api_key and hf_api_key != 'your-huggingface-api-key-here':
            st.success("🤖 AI Features: Active")
        else:
            st.warning("🤖 AI Features: Limited")
            st.info("Add HF API key for full AI features")

    # Route to selected page
    if page == "Dashboard":
        show_dashboard()
    elif page == "AI Chat":
        show_ai_chat()
    elif page == "Expense Tracking":
        show_expense_tracking()
    elif page == "Financial Goals":
        show_financial_goals()
    elif page == "Settings":
        show_settings()

def show_dashboard():
    st.header("📊 Financial Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Balance",
            value=f"${st.session_state.user_profile['balance']:,.2f}",
            delta="+2.5%"
        )
    
    with col2:
        monthly_spending = sum([t['amount'] for t in st.session_state.transactions])
        st.metric(
            label="Monthly Spending",
            value=f"${monthly_spending:,.2f}",
            delta="-15.2%"
        )
    
    with col3:
        savings_goal = 15000
        current_savings = 8200
        st.metric(
            label="Savings Progress",
            value=f"${current_savings:,.2f}",
            delta=f"{(current_savings/savings_goal)*100:.1f}% of goal"
        )
    
    with col4:
        investment_value = 15680
        st.metric(
            label="Investments",
            value=f"${investment_value:,.2f}",
            delta="+5.4%"
        )

    st.markdown("---")

    # Two column layout for charts and insights
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Spending chart
        if st.session_state.transactions:
            df = pd.DataFrame(st.session_state.transactions)
            fig = px.pie(df, values='amount', names='category', title='Spending by Category')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Add some transactions to see spending analysis")
    
    with col2:
        # AI Insights
        st.subheader("🤖 AI Insights")
        show_ai_insights()

def show_ai_insights():
    """Display AI-powered financial insights"""
    insights = generate_ai_insights()
    
    for insight in insights:
        st.markdown(f"""
        <div class="ai-insight">
            <strong>{insight['emoji']} {insight['title']}</strong><br>
            {insight['description']}
        </div>
        """, unsafe_allow_html=True)

def generate_ai_insights():
    """Generate AI insights based on transaction data"""
    insights = []
    
    if not st.session_state.transactions:
        return [{
            'emoji': '💡',
            'title': 'Getting Started',
            'description': 'Add some transactions to get personalized AI insights about your spending patterns!'
        }]
    
    # Analyze spending patterns
    df = pd.DataFrame(st.session_state.transactions)
    total_spent = df['amount'].sum()
    avg_transaction = df['amount'].mean()
    top_category = df.groupby('category')['amount'].sum().idxmax()
    top_amount = df.groupby('category')['amount'].sum().max()
    
    # Generate insights
    insights.append({
        'emoji': '📊',
        'title': 'Top Spending Category',
        'description': f'Your highest spending is in {top_category} with ${top_amount:.2f}'
    })
    
    # Check for large transactions
    large_transactions = df[df['amount'] > avg_transaction * 2]
    if len(large_transactions) > 0:
        insights.append({
            'emoji': '⚠️',
            'title': 'Large Transactions Alert',
            'description': f'You have {len(large_transactions)} unusually large transactions this period'
        })
    
    # Spending trend
    if len(df) >= 3:
        recent_avg = df.tail(3)['amount'].mean()
        if recent_avg > avg_transaction * 1.2:
            insights.append({
                'emoji': '📈',
                'title': 'Spending Trend',
                'description': 'Your recent spending is above average. Consider reviewing your budget.'
            })
        else:
            insights.append({
                'emoji': '🎉',
                'title': 'Great Job!',
                'description': 'Your recent spending is well controlled!'
            })
    
    return insights

def show_ai_chat():
    st.header("🤖 AI Financial Assistant")
    
    # Chat interface
    st.subheader("💬 Chat with your AI Financial Advisor")
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                st.markdown(f"""
                <div style="text-align: right; margin: 1rem 0;">
                    <div style="background: #3b82f6; color: white; padding: 0.5rem 1rem; 
                                border-radius: 1rem; display: inline-block; max-width: 70%;">
                        {message['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="text-align: left; margin: 1rem 0;">
                    <div style="background: #f1f5f9; color: #1f2937; padding: 0.5rem 1rem; 
                                border-radius: 1rem; display: inline-block; max-width: 70%;">
                        🤖 {message['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Chat input
    user_input = st.text_input("Ask me anything about your finances:", key="chat_input")
    
    if st.button("Send", key="send_message") and user_input:
        # Add user message
        st.session_state.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        
        # Generate AI response
        ai_response = generate_ai_response(user_input)
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': ai_response
        })
        
        st.rerun()
    
    # Quick suggestions
    st.subheader("💡 Quick Questions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("How should I budget?"):
            handle_quick_question("How should I budget my income?")
    
    with col2:
        if st.button("Investment advice?"):
            handle_quick_question("What investment advice do you have for me?")
    
    with col3:
        if st.button("Reduce expenses?"):
            handle_quick_question("How can I reduce my expenses?")

def handle_quick_question(question):
    st.session_state.chat_history.append({
        'role': 'user',
        'content': question
    })
    
    ai_response = generate_ai_response(question)
    st.session_state.chat_history.append({
        'role': 'assistant',
        'content': ai_response
    })
    
    st.rerun()

def generate_ai_response(user_input):
    """Generate AI response using Hugging Face or fallback responses"""
    # Try to use Hugging Face API
    try:
        from huggingface_service import get_financial_advice
        return get_financial_advice(user_input)
    except Exception as e:
        # Fallback to static responses
        return get_static_financial_response(user_input)

def get_static_financial_response(message):
    """Static financial responses when AI is not available"""
    message_lower = message.lower()
    
    if 'budget' in message_lower:
        return "Creating a budget is essential! Try the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings and debt repayment."
    
    elif 'save' in message_lower or 'saving' in message_lower:
        return "Great question about saving! Start with an emergency fund of 3-6 months of expenses, then automate transfers to savings accounts."
    
    elif 'invest' in message_lower:
        return "For investing, consider diversifying with low-cost index funds. Think long-term and match your risk tolerance to your investment timeline."
    
    elif 'debt' in message_lower:
        return "For debt management, try the debt avalanche method: pay minimums on all debts, then extra on the highest interest rate debt."
    
    elif 'expense' in message_lower:
        return "To reduce expenses, track everything for a week, identify wants vs needs, and look for subscription services you can cancel."
    
    else:
        return "I'm here to help with budgeting, saving, investing, and debt management. What specific area would you like to discuss?"

def show_expense_tracking():
    st.header("💳 Expense Tracking")
    
    # Add expense form
    with st.expander("➕ Add New Expense", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            merchant = st.text_input("Merchant/Description")
            amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
        
        with col2:
            categories = ["Food & Dining", "Transportation", "Shopping", "Entertainment", 
                         "Bills & Utilities", "Healthcare", "Travel", "Education", "Other"]
            category = st.selectbox("Category", categories)
            date = st.date_input("Date", datetime.now())
        
        with col3:
            payment_methods = ["Credit Card", "Debit Card", "Cash", "Bank Transfer", "Digital Wallet"]
            payment_method = st.selectbox("Payment Method", payment_methods)
            notes = st.text_area("Notes (optional)", height=100)
        
        if st.button("💾 Add Expense", type="primary"):
            if merchant and amount > 0:
                # AI-powered category suggestion
                suggested_category = suggest_category(merchant, notes)
                if suggested_category and suggested_category != category:
                    st.info(f"🤖 AI suggests category: {suggested_category}")
                
                new_expense = {
                    'id': len(st.session_state.transactions) + 1,
                    'merchant': merchant,
                    'amount': amount,
                    'category': category,
                    'date': date.strftime('%Y-%m-%d'),
                    'payment_method': payment_method,
                    'notes': notes,
                    'timestamp': datetime.now()
                }
                
                st.session_state.transactions.append(new_expense)
                st.success("✅ Expense added successfully!")
                st.rerun()
    
    # Display transactions
    if st.session_state.transactions:
        st.subheader("📋 Recent Transactions")
        
        df = pd.DataFrame(st.session_state.transactions)
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            category_filter = st.multiselect("Filter by Category", df['category'].unique())
        with col2:
            amount_range = st.slider("Amount Range", 0, int(df['amount'].max()), (0, int(df['amount'].max())))
        with col3:
            date_range = st.date_input("Date Range", [datetime.now() - timedelta(days=30), datetime.now()])
        
        # Apply filters
        filtered_df = df.copy()
        if category_filter:
            filtered_df = filtered_df[filtered_df['category'].isin(category_filter)]
        
        filtered_df = filtered_df[
            (filtered_df['amount'] >= amount_range[0]) & 
            (filtered_df['amount'] <= amount_range[1])
        ]
        
        # Display transactions
        for _, transaction in filtered_df.iterrows():
            st.markdown(f"""
            <div class="expense-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong>{transaction['merchant']}</strong><br>
                        <small>{transaction['category']} • {transaction['date']}</small>
                    </div>
                    <div style="text-align: right;">
                        <strong style="font-size: 1.2em;">${transaction['amount']:.2f}</strong><br>
                        <small>{transaction['payment_method']}</small>
                    </div>
                </div>
                {f"<p style='margin-top: 0.5rem; color: #6b7280;'>{transaction['notes']}</p>" if transaction['notes'] else ""}
            </div>
            """, unsafe_allow_html=True)
        
        # Summary statistics
        st.subheader("📊 Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Spent", f"${filtered_df['amount'].sum():.2f}")
        with col2:
            st.metric("Average Transaction", f"${filtered_df['amount'].mean():.2f}")
        with col3:
            st.metric("Number of Transactions", len(filtered_df))
        with col4:
            st.metric("Largest Expense", f"${filtered_df['amount'].max():.2f}")
    
    else:
        st.info("No transactions yet. Add your first expense above!")

def suggest_category(merchant, notes=""):
    """AI-powered category suggestion"""
    # Simple keyword-based categorization (fallback)
    text = f"{merchant} {notes}".lower()
    
    if any(word in text for word in ['restaurant', 'coffee', 'food', 'pizza', 'burger', 'starbucks']):
        return "Food & Dining"
    elif any(word in text for word in ['gas', 'uber', 'taxi', 'bus', 'train', 'parking']):
        return "Transportation"
    elif any(word in text for word in ['amazon', 'target', 'walmart', 'shopping', 'store']):
        return "Shopping"
    elif any(word in text for word in ['netflix', 'spotify', 'movie', 'entertainment', 'game']):
        return "Entertainment"
    elif any(word in text for word in ['electric', 'water', 'internet', 'phone', 'utility', 'bill']):
        return "Bills & Utilities"
    elif any(word in text for word in ['doctor', 'hospital', 'pharmacy', 'medical', 'health']):
        return "Healthcare"
    else:
        return "Other"

def show_financial_goals():
    st.header("🎯 Financial Goals")
    
    # Add goal form
    with st.expander("➕ Add New Goal", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            goal_name = st.text_input("Goal Name")
            target_amount = st.number_input("Target Amount ($)", min_value=1.0, step=100.0)
            current_amount = st.number_input("Current Amount ($)", min_value=0.0, step=10.0)
        
        with col2:
            goal_types = ["Emergency Fund", "Vacation", "Car", "House", "Investment", "Education", "Other"]
            goal_type = st.selectbox("Goal Type", goal_types)
            target_date = st.date_input("Target Date", datetime.now() + timedelta(days=365))
            monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0.0, step=25.0)
        
        if st.button("🎯 Add Goal", type="primary"):
            if goal_name and target_amount > 0:
                new_goal = {
                    'id': len(st.session_state.goals) + 1,
                    'name': goal_name,
                    'type': goal_type,
                    'target_amount': target_amount,
                    'current_amount': current_amount,
                    'target_date': target_date.strftime('%Y-%m-%d'),
                    'monthly_contribution': monthly_contribution,
                    'created_date': datetime.now().strftime('%Y-%m-%d')
                }
                
                st.session_state.goals.append(new_goal)
                st.success("✅ Goal added successfully!")
                st.rerun()
    
    # Display goals
    if st.session_state.goals:
        st.subheader("📈 Your Goals")
        
        for goal in st.session_state.goals:
            progress = (goal['current_amount'] / goal['target_amount']) * 100
            remaining = goal['target_amount'] - goal['current_amount']
            
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; 
                        box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <h3 style="margin: 0; color: #1f2937;">{goal['name']}</h3>
                    <span style="background: #3b82f6; color: white; padding: 0.25rem 0.75rem; 
                                border-radius: 1rem; font-size: 0.875rem;">{goal['type']}</span>
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <div style="background: #e5e7eb; height: 0.5rem; border-radius: 0.25rem; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, #10b981, #059669); height: 100%; 
                                    width: {min(progress, 100)}%; transition: width 0.3s ease;"></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-top: 0.5rem; font-size: 0.875rem; color: #6b7280;">
                        <span>${goal['current_amount']:,.2f} of ${goal['target_amount']:,.2f}</span>
                        <span>{progress:.1f}% complete</span>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; font-size: 0.875rem;">
                    <div>
                        <strong>Remaining:</strong><br>
                        ${remaining:,.2f}
                    </div>
                    <div>
                        <strong>Target Date:</strong><br>
                        {goal['target_date']}
                    </div>
                    <div>
                        <strong>Monthly Goal:</strong><br>
                        ${goal['monthly_contribution']:,.2f}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Add progress button
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button(f"Add Progress", key=f"progress_{goal['id']}"):
                    contribution = st.number_input(
                        f"Add to {goal['name']}", 
                        min_value=0.01, 
                        step=10.0, 
                        key=f"contrib_{goal['id']}"
                    )
                    if contribution:
                        # Update goal progress
                        for i, g in enumerate(st.session_state.goals):
                            if g['id'] == goal['id']:
                                st.session_state.goals[i]['current_amount'] += contribution
                                break
                        st.success(f"Added ${contribution:.2f} to {goal['name']}!")
                        st.rerun()
    else:
        st.info("No goals set yet. Add your first financial goal above!")

def show_settings():
    st.header("⚙️ Settings")
    
    # User profile settings
    st.subheader("👤 User Profile")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", value=st.session_state.user_profile['name'])
        user_type = st.selectbox("User Type", ["professional", "student"], 
                                index=0 if st.session_state.user_profile['type'] == 'professional' else 1)
    
    with col2:
        balance = st.number_input("Current Balance ($)", 
                                 value=st.session_state.user_profile['balance'], 
                                 step=100.0)
    
    if st.button("💾 Save Profile"):
        st.session_state.user_profile.update({
            'name': name,
            'type': user_type,
            'balance': balance
        })
        st.success("Profile updated successfully!")
    
    st.markdown("---")
    
    # AI Configuration
    st.subheader("🤖 AI Configuration")
    
    hf_api_key = st.text_input("Hugging Face API Key", 
                              value=os.getenv('HUGGINGFACE_API_KEY', ''),
                              type="password",
                              help="Get your API key from https://huggingface.co/settings/tokens")
    
    if st.button("🔑 Save API Key"):
        # In a real app, you'd save this securely
        st.success("API key configuration updated!")
        st.info("Restart the application to apply changes.")
    
    st.markdown("---")
    
    # Data Management
    st.subheader("💾 Data Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📤 Export Data"):
            # Export data as JSON
            export_data = {
                'transactions': st.session_state.transactions,
                'goals': st.session_state.goals,
                'user_profile': st.session_state.user_profile
            }
            st.download_button(
                label="Download Data",
                data=json.dumps(export_data, indent=2),
                file_name=f"finance_bot_data_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    with col2:
        uploaded_file = st.file_uploader("📥 Import Data", type="json")
        if uploaded_file and st.button("Import"):
            try:
                import_data = json.load(uploaded_file)
                st.session_state.transactions = import_data.get('transactions', [])
                st.session_state.goals = import_data.get('goals', [])
                st.session_state.user_profile.update(import_data.get('user_profile', {}))
                st.success("Data imported successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Import failed: {str(e)}")
    
    with col3:
        if st.button("🗑️ Clear All Data", type="secondary"):
            if st.checkbox("I understand this will delete all data"):
                st.session_state.transactions = []
                st.session_state.goals = []
                st.session_state.chat_history = []
                st.success("All data cleared!")
                st.rerun()

if __name__ == "__main__":
    main()
