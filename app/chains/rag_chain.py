from langchain_core.output_parsers import StrOutputParser

from app.models.gemini_model import model
from app.prompt.rag_prompt import rag_prompt

# RAG returns plain conversational text — must use StrOutputParser, NOT JsonOutputParser
chain = rag_prompt | model | StrOutputParser()