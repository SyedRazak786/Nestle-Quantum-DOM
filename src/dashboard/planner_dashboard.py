"""
planner_dashboard.py
--------------------------------
Main Dashboard

Author: SYED RAZAK
"""

import streamlit as st

from home import show_home
from data_engineering import show_data_engineering
from ai_prediction import show_ai_prediction
from classical import show_classical
from quantum import show_quantum
from evaluation import show_evaluation
from business_strategy import show_business_strategy
from downloads import show_downloads


st.set_page_config(
    page_title="Nestlé Quantum DOM",
    page_icon="📦",
    layout="wide"
)

st.sidebar.title("📦 Nestlé Quantum DOM")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Data Engineering",
        "🤖 AI Prediction",
        "⚙️ Classical Optimization",
        "⚛️ Quantum Optimization",
        "📈 Evaluation",
        "💼 Business Strategy",
        "📥 Downloads",
    ]
)

if page == "🏠 Home":
    show_home()

elif page == "📊 Data Engineering":
    show_data_engineering()

elif page == "🤖 AI Prediction":
    show_ai_prediction()

elif page == "⚙️ Classical Optimization":
    show_classical()

elif page == "⚛️ Quantum Optimization":
    show_quantum()

elif page == "📈 Evaluation":
    show_evaluation()

elif page == "💼 Business Strategy":
    show_business_strategy()    

elif page == "📥 Downloads":
    show_downloads()
