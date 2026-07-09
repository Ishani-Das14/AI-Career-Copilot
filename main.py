from app.models.gemini_model import model
from app.prompt.basic_prompt import prompt
from app.parsers.output_parser import parser
from langchain_core.messages import SystemMessage, HumanMessage

formatted_prompt = prompt.invoke(
    {
        "question": "Give me 5 study tips to be better"
    }
)

chain = prompt | model | parser

response = chain.invoke(
    {
        "question": "Give me 5 study tips to be better"
    }
)

print(response)
