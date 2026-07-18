import os
import tempfile

import streamlit as st

from app.services.rag_service import create_retriever, ask_question_with_retriever


def render_chat_card():
    """Render the Resume AI Assistant."""

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Streamlit auto-populates st.session_state["resume"] because the file_uploader
    # in ats_card.py uses key="resume". We just read it here — never write to it.
    resume = st.session_state.get("resume")

    with st.container(border=True):

        # -----------------------------------
        # Header
        # -----------------------------------

        st.subheader("💬 Resume AI Assistant")

        st.markdown(
            """
Your personal AI assistant for resumes, career guidance,
interview preparation, and ATS optimization.
"""
        )

        st.divider()

        # -----------------------------------
        # Chat Area
        # -----------------------------------

        chat_container = st.container(height=320)

        with chat_container:

            if len(st.session_state.chat_history) == 0:

                with st.chat_message("assistant"):

                    st.markdown(
"""
## 👋 Welcome!

I can help you with:

- 📄 Resume Review
- 🎯 ATS Optimization
- 🧠 Career Guidance
- 💼 Job Matching
- 🚀 Project Suggestions

Upload your resume and ask me anything to get started.
"""
                    )

            else:

                for role, message in st.session_state.chat_history:

                    with st.chat_message(role):
                        st.markdown(message)

        st.write("")

        st.divider()

        # -----------------------------------
        # User Input
        # -----------------------------------

        question = st.text_input(
            "Ask your question",
            placeholder="Example: How can I improve my ATS score?",
            key="question",
        )

        ask = st.button(
            "✨ Ask AI",
            use_container_width=True,
        )

        if ask:

            if question.strip() == "":
                st.warning("Please enter a question.")

            elif not resume:
                st.error("📂 Please upload your resume in the **ATS Resume Analyzer** panel first.")

            else:

                # -----------------------------------
                # Build retriever once, cache it in session state
                # -----------------------------------

                if "retriever" not in st.session_state:

                    with st.spinner("🧠 Indexing your resume for the first time..."):

                        with tempfile.NamedTemporaryFile(
                            delete=False,
                            suffix=".pdf",
                        ) as temp_pdf:
                            temp_pdf.write(resume.getbuffer())
                            temp_path = temp_pdf.name

                        try:
                            st.session_state["retriever"] = create_retriever(temp_path)
                        finally:
                            if os.path.exists(temp_path):
                                os.remove(temp_path)

                # -----------------------------------
                # Ask the Real Backend
                # -----------------------------------

                st.session_state.chat_history.append(("user", question))

                try:

                    with st.spinner("🤖 AI is thinking..."):

                        response = ask_question_with_retriever(
                            st.session_state["retriever"],
                            question,
                        )

                    st.session_state.chat_history.append(("assistant", response))

                except Exception as e:

                    st.session_state.chat_history.append(
                        ("assistant", f"⚠️ Sorry, an error occurred: {e}")
                    )

                st.rerun()