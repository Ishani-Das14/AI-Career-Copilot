import streamlit as st


def show_dashboard():

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📄 Resume",
            value="Not Uploaded"
        )

    with col2:
        st.metric(
            label="📊 ATS Score",
            value="--"
        )

    with col3:
        st.metric(
            label="🤖 AI Assistant",
            value="Ready"
        )