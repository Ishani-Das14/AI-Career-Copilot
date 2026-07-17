from app.services.ats_service import analyze_resume
from app.services.rag_service import ask_question


def display_menu():
    print("\n" + "=" * 45)
    print("         AI Career Copilot")
    print("=" * 45)
    print("1. ATS Resume Analysis")
    print("2. Resume Chat")
    print("3. Exit")


while True:

    display_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":

        response = analyze_resume(
            resume_path="data/resume.txt",
            job_description_path="data/job_description.txt"
        )

        print("\nATS Review:\n")
        print(response)

        input("\nPress Enter to return to the menu...")

    elif choice == "2":

        question = input("\nAsk a question about your resume: ")

        response = ask_question(
            pdf_path="data/resume.pdf",
            question=question
        )

        print("\nAnswer:\n")
        print(response)

        input("\nPress Enter to return to the menu...")

    elif choice == "3":

        print("\nThank you for using AI Career Copilot!")
        break

    else:

        print("\n Invalid choice. Please try again.")