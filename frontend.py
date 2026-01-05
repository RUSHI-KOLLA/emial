import streamlit as st
import requests
import pandas as pd

# Page Config
st.set_page_config(page_title="Email Classifier", page_icon="📩")

# CSS
st.markdown("""
    <style>
    .stTextArea textarea {font-size: 16px;}
    .main-header {font-size: 40px; font-weight: bold; color: #4F8BF9;}
    </style>
    """, unsafe_allow_html=True)

# Session State for History
if 'history' not in st.session_state:
    st.session_state.history = []

def get_category_style(category):
    styles = {
        "Promotions": "🏷️ Promotions",
        "Social":     "👥 Social",
        "Updates":    "🔔 Updates",
        "Primary":    "👔 Primary"
    }
    return styles.get(category, "❓ Unknown")

st.markdown('<p class="main-header">📧 Intelligent Email Classifier</p>', unsafe_allow_html=True)

# Input Form
subject = st.text_input("Subject Line")
body = st.text_area("Email Body", height=200)

if st.button("🔍 Classify Email", use_container_width=True):
    if not subject or not body:
        st.warning("Please enter both subject and body.")
    else:
        with st.spinner("Analyzing..."):
            try:
                # CONNECT TO BACKEND
                response = requests.post("http://127.0.0.1:8000/predict", json={"subject": subject, "body": body})
                
                if response.status_code == 200:
                    cat = response.json().get('category', 'Error')
                    st.success(f"## {get_category_style(cat)}")
                    st.session_state.history.insert(0, {"Subject": subject, "Category": cat})
                else:
                    st.error("Backend error.")
            except:
                st.error("Could not connect to backend. Is uvicorn running?")

# Sidebar History
st.sidebar.header("Recent History")
if st.session_state.history:
    st.sidebar.dataframe(pd.DataFrame(st.session_state.history), hide_index=True)