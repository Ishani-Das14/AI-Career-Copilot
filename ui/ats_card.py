import streamlit as st


def render_ats_card():
    """Render the ATS Resume Analyzer."""

    with st.container(border=True):

        # -----------------------------------
        # Header
        # -----------------------------------

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

        # -----------------------------------
        # Resume Upload
        # -----------------------------------

        st.markdown("### 📄 Resume")

        st.caption("Upload your latest resume (PDF only)")

        resume = st.file_uploader(
            "Choose Resume",
            type=["pdf"],
            key="resume",
            label_visibility="collapsed",
        )

        if resume is not None:
            st.success(f"✅ {resume.name}")

        st.write("")

        # -----------------------------------
        # Job Description Upload
        # -----------------------------------

        st.markdown("### 📋 Job Description")

        st.caption("Upload the target job description (PDF or TXT)")

        jd = st.file_uploader(
            "Choose Job Description",
            type=["pdf", "txt"],
            key="job_description",
            label_visibility="collapsed",
        )

        if jd is not None:
            st.success(f"✅ {jd.name}")

        st.write("")

        st.divider()

        # -----------------------------------
        # Analyze Button
        # -----------------------------------

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True,
        )

        if analyze:

            if resume is None:
                st.error("Please upload your resume.")
                return

            if jd is None:
                st.error("Please upload the job description.")
                return

            with st.spinner("🤖 AI is analyzing your resume..."):

                # Temporary Data
                st.session_state["ats_results"] = {
                    "score": 87,
                    "summary": "Excellent match for the selected role.",

                    "matching_skills": [
                        "Python",
                        "Machine Learning",
                        "SQL",
                        "TensorFlow",
                        "Scikit-Learn",
                    ],

                    "missing_skills": [
                        "Docker",
                        "AWS",
                        "Kubernetes",
                    ],

                    "strengths": [
                        "Strong AI Projects",
                        "Relevant Internship Experience",
                        "Good Technical Skills",
                    ],

                    "improvements": [
                        "Add measurable achievements",
                        "Mention Cloud technologies",
                        "Improve ATS keywords",
                    ],

                    "suggestions": [
                        "Customize resume for every job.",
                        "Add Docker experience.",
                        "Use more action verbs.",
                    ],
                }

            st.success("✨ Analysis Complete!")