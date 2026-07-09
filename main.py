from app.models.gemini_model import model
from app.prompt.ats_resume_prompt import ats_resume_prompt
from app.parsers.output_parser import parser
from app.services.file_reader import read_text_file

chain = ats_resume_prompt | model | parser

resume = read_text_file("data/resume.txt")
job_description = read_text_file("data/job_description.txt")


response = chain.invoke(
    {
        "resume": resume,
        "job_description": job_description
    }
)

print(response)
