from langchain_core.prompts import ChatPromptTemplate

ats_resume_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert ATS Resume Reviewer.

Compare the provided resume with the given job description.

Evaluate based on:
- Skills
- Experience
- Education
- Relevant Keywords

Return ONLY valid JSON.

Do NOT add explanations.
Do NOT use markdown.
Do NOT wrap the JSON in ```.

The JSON format must be:

{{
    "score": 0,
    "summary": "",
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "improvements": [],
    "suggestions": []
}}

Rules:
- score must be an integer from 0 to 100.
- Every list should contain 3–7 concise items.
- summary should be 2–3 sentences.
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
        ),
    ]
)