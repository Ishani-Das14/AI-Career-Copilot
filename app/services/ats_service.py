from app.models.gemini_model import model
from app.prompt.ats_resume_prompt import ats_resume_prompt
from app.parsers.output_parser import parser
from app.services.file_reader import read_document

chain = ats_resume_prompt | model | parser


def analyze_resume(resume_path, job_description_path):
    print("=" * 60)
    print("[ATS] Service Called")

    # Read files
    resume = read_document(resume_path)
    job_description = read_document(job_description_path)

    print("[ATS] Resume Loaded")
    print("[ATS] Resume Length:", len(resume))

    print("[ATS] Job Description Loaded")
    print("[ATS] JD Length:", len(job_description))

    # Call Gemini
    response = chain.invoke(
        {
            "resume": resume,
            "job_description": job_description,
        }
    )

    print("\n[ATS] Gemini Response:")
    print(response)
    print("=" * 60)

    return response