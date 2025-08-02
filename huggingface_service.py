"""
Hugging Face Service for Streamlit Finance Bot
Provides AI-powered financial analysis and advice
"""

import os
import requests
import time
from typing import List, Dict, Any, Optional
import streamlit as st

class HuggingFaceService:
    def __init__(self):
        self.api_key = os.getenv('HUGGINGFACE_API_KEY')
        self.base_url = 'https://api-inference.huggingface.co/models'
        
        # Financial-focused models
        self.models = {
            'text_generation': 'microsoft/DialoGPT-medium',
            'sentiment': 'ProsusAI/finbert',
            'question_answering': 'deepset/roberta-base-squad2',
            'classification': 'facebook/bart-large-mnli',
            'summarization': 'facebook/bart-large-cnn'
        }
    
    def _make_request(self, model: str, payload: Dict[str, Any], retries: int = 3) -> Optional[Dict]:
        """Make API request with error handling and retries"""
        if not self.api_key or self.api_key == 'your-huggingface-api-key-here':
            return None
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        url = f"{self.base_url}/{model}"
        
        for attempt in range(retries):
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 503:
                    # Model is loading, wait and retry
                    if attempt < retries - 1:
                        time.sleep(20)
                        continue
                
                if response.status_code == 200:
                    return response.json()
                else:
                    st.warning(f"API request failed with status {response.status_code}")
                    return None
                    
            except requests.exceptions.RequestException as e:
                if attempt < retries - 1:
                    time.sleep(5)
                    continue
                st.error(f"Request failed: {str(e)}")
                return None
        
        return None
    
    def generate_financial_advice(self, query: str, context: str = "") -> str:
        """Generate financial advice using text generation"""
        try:
            prompt = f"Financial Query: {query}\nContext: {context}\nAdvice:"
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_length": 200,
                    "temperature": 0.7,
                    "do_sample": True,
                    "pad_token_id": 50256
                }
            }
            
            response = self._make_request(self.models['text_generation'], payload)
            
            if response and isinstance(response, list) and len(response) > 0:
                generated_text = response[0].get('generated_text', '')
                advice = generated_text.replace(prompt, '').strip()
                if advice:
                    return advice
            
            # Fallback to static response
            return self._get_static_advice(query)
            
        except Exception as e:
            st.error(f"Error generating advice: {str(e)}")
            return self._get_static_advice(query)
    
    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment of financial text"""
        try:
            payload = {"inputs": text}
            response = self._make_request(self.models['sentiment'], payload)
            
            if response and isinstance(response, list) and len(response) > 0:
                result = response[0]
                return {
                    'label': result.get('label', 'neutral'),
                    'score': result.get('score', 0.5),
                    'confidence': 'high' if result.get('score', 0) > 0.8 else 
                                'medium' if result.get('score', 0) > 0.5 else 'low'
                }
            
            return {'label': 'neutral', 'score': 0.5, 'confidence': 'low'}
            
        except Exception as e:
            st.error(f"Error analyzing sentiment: {str(e)}")
            return {'label': 'neutral', 'score': 0.5, 'confidence': 'low'}
    
    def classify_expense(self, description: str, categories: List[str]) -> Dict[str, Any]:
        """Classify expense into categories"""
        try:
            payload = {
                "inputs": description,
                "parameters": {
                    "candidate_labels": categories
                }
            }
            
            response = self._make_request(self.models['classification'], payload)
            
            if response and 'labels' in response and 'scores' in response:
                return {
                    'category': response['labels'][0],
                    'confidence': response['scores'][0],
                    'all_categories': [
                        {'category': label, 'confidence': score}
                        for label, score in zip(response['labels'], response['scores'])
                    ]
                }
            
            # Fallback to keyword-based classification
            return self._classify_expense_fallback(description, categories)
            
        except Exception as e:
            st.error(f"Error classifying expense: {str(e)}")
            return self._classify_expense_fallback(description, categories)
    
    def summarize_text(self, text: str, max_length: int = 100) -> str:
        """Summarize financial text"""
        try:
            payload = {
                "inputs": text,
                "parameters": {
                    "max_length": max_length,
                    "min_length": 30,
                    "do_sample": False
                }
            }
            
            response = self._make_request(self.models['summarization'], payload)
            
            if response and isinstance(response, list) and len(response) > 0:
                return response[0].get('summary_text', 'Unable to summarize text.')
            
            return 'Unable to summarize text.'
            
        except Exception as e:
            st.error(f"Error summarizing text: {str(e)}")
            return 'Error occurred while summarizing.'
    
    def get_financial_insights(self, transactions: List[Dict[str, Any]]) -> List[str]:
        """Generate financial insights from transaction data"""
        try:
            if not transactions:
                return ["Add some transactions to get AI-powered insights!"]
            
            insights = []
            total_spent = sum(t.get('amount', 0) for t in transactions)
            avg_transaction = total_spent / len(transactions) if transactions else 0
            
            # Category analysis
            categories = {}
            for t in transactions:
                cat = t.get('category', 'Other')
                categories[cat] = categories.get(cat, 0) + t.get('amount', 0)
            
            if categories:
                top_category = max(categories.keys(), key=lambda k: categories[k])
                insights.append(f"Your highest spending category is {top_category} with ${categories[top_category]:.2f}")
            
            # Large transaction analysis
            large_transactions = [t for t in transactions if t.get('amount', 0) > avg_transaction * 2]
            if large_transactions:
                insights.append(f"You had {len(large_transactions)} unusually large transaction(s) this period")
            
            # Recent spending trend
            if len(transactions) > 3:
                recent = transactions[-3:]
                recent_avg = sum(t.get('amount', 0) for t in recent) / len(recent)
                
                if recent_avg > avg_transaction * 1.2:
                    insights.append("Your recent spending is above average. Consider reviewing your budget.")
                elif recent_avg < avg_transaction * 0.8:
                    insights.append("Great job! Your recent spending is below average.")
            
            return insights if insights else ["Your spending patterns look normal."]
            
        except Exception as e:
            st.error(f"Error generating insights: {str(e)}")
            return ["Unable to generate insights at this time."]
    
    def _get_static_advice(self, query: str) -> str:
        """Static financial advice fallback"""
        query_lower = query.lower()
        
        if 'budget' in query_lower:
            return "Creating a budget is essential for financial health. Start with the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings and debt repayment."
        
        elif 'save' in query_lower or 'saving' in query_lower:
            return "Start by setting up an emergency fund with 3-6 months of expenses. Then consider automated transfers to savings accounts for your goals."
        
        elif 'invest' in query_lower:
            return "Investment basics: diversify your portfolio, start with low-cost index funds, and think long-term. Consider your risk tolerance and investment timeline."
        
        elif 'debt' in query_lower:
            return "For debt management, consider the debt avalanche method (pay minimums on all debts, extra on highest interest) or debt snowball (smallest balance first)."
        
        elif 'goal' in query_lower:
            return "Financial goals should be SMART: Specific, Measurable, Achievable, Relevant, and Time-bound. Break large goals into smaller milestones."
        
        else:
            return "I'm here to help with budgeting, saving, investing, debt management, and setting financial goals. What specific area interests you?"
    
    def _classify_expense_fallback(self, description: str, categories: List[str]) -> Dict[str, Any]:
        """Fallback expense classification using keywords"""
        text = description.lower()
        
        # Keyword mapping
        keyword_map = {
            'food & dining': ['restaurant', 'coffee', 'food', 'pizza', 'burger', 'starbucks', 'mcdonalds'],
            'transportation': ['gas', 'uber', 'taxi', 'bus', 'train', 'parking', 'fuel'],
            'shopping': ['amazon', 'target', 'walmart', 'shopping', 'store', 'mall'],
            'entertainment': ['netflix', 'spotify', 'movie', 'entertainment', 'game', 'theater'],
            'bills & utilities': ['electric', 'water', 'internet', 'phone', 'utility', 'bill'],
            'healthcare': ['doctor', 'hospital', 'pharmacy', 'medical', 'health']
        }
        
        # Find best match
        best_category = 'Other'
        best_confidence = 0.3
        
        for category, keywords in keyword_map.items():
            if category.lower() in [c.lower() for c in categories]:
                matches = sum(1 for keyword in keywords if keyword in text)
                if matches > 0:
                    confidence = min(0.9, 0.5 + (matches * 0.1))
                    if confidence > best_confidence:
                        best_category = category.title()
                        best_confidence = confidence
        
        return {
            'category': best_category,
            'confidence': best_confidence,
            'all_categories': [{'category': best_category, 'confidence': best_confidence}]
        }

# Global service instance
hf_service = HuggingFaceService()

# Convenience functions for Streamlit app
def get_financial_advice(query: str, context: str = "") -> str:
    """Get financial advice from AI or fallback"""
    return hf_service.generate_financial_advice(query, context)

def analyze_expense_sentiment(text: str) -> Dict[str, Any]:
    """Analyze sentiment of expense description"""
    return hf_service.analyze_sentiment(text)

def categorize_expense(description: str, categories: List[str]) -> Dict[str, Any]:
    """Categorize expense using AI"""
    return hf_service.classify_expense(description, categories)

def get_spending_insights(transactions: List[Dict[str, Any]]) -> List[str]:
    """Get AI insights from spending data"""
    return hf_service.get_financial_insights(transactions)

def summarize_financial_text(text: str, max_length: int = 100) -> str:
    """Summarize financial text"""
    return hf_service.summarize_text(text, max_length)
