from app.models.gemini_model import model
from app.prompt.basic_prompt import prompt
from langchain_core.messages import SystemMessage, HumanMessage

formatted_prompt = prompt.invoke(
    {
        "question": "Give me 5 study tips to be better"
    }
)

chain = prompt | model

response = chain.invoke(
    {
        "question": "Give me 5 study tips to be better"
    }
)

print(response.content)
