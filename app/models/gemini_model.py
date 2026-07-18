# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=api_key,
#     temperature=0.2,
# )
import traceback

print(">>> Loading gemini_model.py")

try:
    import os
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    print("API Key Found:", bool(api_key))

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.2,
    )

    print(">>> Gemini model created successfully")

except Exception:
    print(">>> ERROR INSIDE gemini_model.py")
    traceback.print_exc()
    raise