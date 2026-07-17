import streamlit as st


def render_results():
    """Render ATS Analysis Results."""

    results = st.session_state.get("ats_results")

    if results is None:
        return

    st.write("")
    st.write("")

    st.markdown("# 📊 ATS Analysis Report")
    st.caption("AI-generated insights based on your resume and job description.")

    st.divider()

    # =========================================
    # Score + Summary
    # =========================================

    left, right = st.columns([1, 3], gap="large")

    with left:

        st.metric(
            label="ATS Score",
            value=f"{results['score']}%",
        )

        st.progress(results["score"] / 100)

    with right:

        st.markdown("### 📝 Summary")

        st.success(results["summary"])

    st.write("")
    st.divider()

    # =========================================
    # Skills
    # =========================================

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("### 🟢 Matching Skills")

        for skill in results["matching_skills"]:
            st.success(skill)

    with col2:

        st.markdown("### 🔴 Missing Skills")

        for skill in results["missing_skills"]:
            st.error(skill)

    st.write("")
    st.divider()

    # =========================================
    # Strengths
    # =========================================

    st.markdown("### 💪 Strengths")

    for strength in results["strengths"]:
        st.info(f"✅ {strength}")

    st.write("")

    # =========================================
    # Improvements
    # =========================================

    st.markdown("### 🚀 Improvements")

    for improvement in results["improvements"]:
        st.warning(f"⚡ {improvement}")

    st.write("")

    # =========================================
    # AI Suggestions
    # =========================================

    st.markdown("### 🤖 AI Suggestions")

    for suggestion in results["suggestions"]:
        st.markdown(f"- {suggestion}")