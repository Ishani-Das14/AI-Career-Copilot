import streamlit as st


def render_chat_card():
    """Render the Resume AI Assistant."""

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

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

Ask me anything to get started.
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

            else:

                st.session_state.chat_history.append(
                    ("user", question)
                )

                # -----------------------------------
                # Temporary AI Response
                # -----------------------------------

                response = """
Your resume demonstrates a strong AI/ML foundation.

### Suggestions

✅ Add measurable achievements.

✅ Mention Docker and Cloud technologies.

✅ Improve ATS keyword matching.

✅ Expand project descriptions with measurable impact.
"""

                st.session_state.chat_history.append(
                    ("assistant", response)
                )

                st.rerun()