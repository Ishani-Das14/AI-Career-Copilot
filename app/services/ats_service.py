from app.models.gemini_model import model
from app.prompt.ats_resume_prompt import ats_resume_prompt
from app.parsers.output_parser import parser
from app.services.file_reader import read_text_file

chain = ats_resume_prompt | model | parser


def analyze_resume(resume_path, job_description_path):

    resume = read_text_file(resume_path)

    job_description = read_text_file(job_description_path)

    response = chain.invoke(
        {
            "resume": resume,
            "job_description": job_description
        }
    )

    return response