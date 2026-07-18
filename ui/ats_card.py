import os
import tempfile

import streamlit as st

from app.services.ats_service import analyze_resume


def _on_resume_change():
    """
    Callback fired by Streamlit when the resume file_uploader changes.
    Callbacks are the ONLY safe place to write to session_state after a widget
    has been instantiated. We use this to invalidate the cached FAISS retriever
    whenever a new resume is uploaded.
    """
    st.session_state.pop("retriever", None)


def render_ats_card():
    """Render the ATS Resume Analyzer."""

    with st.container(border=True):

        st.subheader("📄 ATS Resume Analyzer")

        st.markdown(
            """
Get an AI-powered analysis of how well your resume matches a job description.

Upload both files below and receive:

- ✅ ATS Compatibility Score
- 🎯 Skill Gap Analysis
- 💡 Personalized AI Suggestions
"""
        )

        st.divider()

        # Resume Upload
        st.markdown("### 📄 Resume")

        resume = st.file_uploader(
            "Choose Resume",
            type=["pdf"],
            key="resume",
            label_visibility="collapsed",
            on_change=_on_resume_change,   # ← clears retriever cache safely
        )

        if resume:
            st.success(f"✅ {resume.name}")

        st.write("")

        # Job Description Upload
        st.markdown("### 📋 Job Description")

        jd = st.file_uploader(
            "Choose Job Description",
            type=["pdf", "txt"],
            key="job_description",
            label_visibility="collapsed",
        )

        if jd:
            st.success(f"✅ {jd.name}")

        st.write("")
        st.divider()

        if st.button("🚀 Analyze Resume", use_container_width=True):

            if resume is None:
                st.error("Please upload a resume.")
                return

            if jd is None:
                st.error("Please upload a job description.")
                return

            try:

                with st.spinner("🤖 AI is analyzing your resume..."):

                    # Save Resume
                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=os.path.splitext(resume.name)[1],
                    ) as temp_resume:

                        temp_resume.write(resume.getbuffer())
                        resume_path = temp_resume.name

                    # Save Job Description
                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=os.path.splitext(jd.name)[1],
                    ) as temp_jd:

                        temp_jd.write(jd.getbuffer())
                        jd_path = temp_jd.name

                    # REAL BACKEND CALL
                    results = analyze_resume(
                        resume_path,
                        jd_path,
                    )

                    st.session_state["ats_results"] = results

                st.success("✅ Analysis Complete!")

            except Exception as e:

                st.exception(e)

            finally:

                if "resume_path" in locals() and os.path.exists(resume_path):
                    os.remove(resume_path)

                if "jd_path" in locals() and os.path.exists(jd_path):
                    os.remove(jd_path)