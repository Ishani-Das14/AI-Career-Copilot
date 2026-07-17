import streamlit as st


def render_header():

    st.markdown(
        "<h1 style='text-align:center; font-size:70px; margin-bottom:0;'>🤖</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 style='text-align:center; font-size:56px; margin-top:0;'>AI Career Copilot</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='text-align:center; color:#60A5FA; margin-top:-10px;'>Your Personal AI Resume Coach</h3>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center; color:#A1A1AA; font-size:18px; max-width:760px; margin:auto;'>"
        "Optimize your resume, improve ATS scores, identify missing skills, "
        "prepare for interviews, and receive AI-powered career guidance."
        "</p>",
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()