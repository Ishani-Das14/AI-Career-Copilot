from app.services.ats_service import analyze_resume
from app.services.rag_service import ask_question

print("========== AI Career Copilot ==========")
print("1. ATS Resume Analysis")
print("2. Resume Chat")

choice = input("\nChoose an option: ")

if choice == "1":

    response = analyze_resume(
        resume_path="data/resume.txt",
        job_description_path="data/job_description.txt"
    )

    print("\nATS Review:\n")
    print(response)

elif choice == "2":

    question = input("\nAsk a question about your resume: ")

    response = ask_question(
        pdf_path="data/resume.pdf",
        question=question
    )

    print("\nAnswer:\n")
    print(response)

else:
    print("Invalid choice.")