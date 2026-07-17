import streamlit as st

from ui.styles import load_css
from ui.header import render_header
from ui.ats_card import render_ats_card
from ui.chat_card import render_chat_card
from ui.result_card import render_results


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide",
)


# ==========================================
# Load Global CSS
# ==========================================

load_css()


# ==========================================
# Session State
# ==========================================

if "ats_results" not in st.session_state:
    st.session_state.ats_results = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ==========================================
# Header
# ==========================================

render_header()


# ==========================================
# Main Content
# ==========================================

left_col, right_col = st.columns(
    [1, 1],
    gap="large"
)

with left_col:
    render_ats_card()

with right_col:
    render_chat_card()


# ==========================================
# Results
# ==========================================

if st.session_state.ats_results is not None:
    st.write("")
    render_results()