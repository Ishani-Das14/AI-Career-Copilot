from langchain_core.prompts import ChatPromptTemplate

ats_resume_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an experienced ATS Resume Reviewer.

            Compare the provided resume with the given job description.

            Evaluate the resume based on:
            - Skills
            - Experience
            - Education
            - Relevant Keywords

            Provide:

            1. ATS Score (out of 100)
            2. Strengths
            3. Missing Skills
            4. Areas for Improvement
            5. Suggestions to improve the resume according to the job description.
            """
        ),
        (
            "human",
            """
            Resume:
            {resume}

            Job Description:
            {job_description}
            """
        )
    ]
)