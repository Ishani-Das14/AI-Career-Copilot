from app.models.gemini_model import model
from app.prompt.rag_prompt import rag_prompt
from app.parsers.output_parser import parser

chain = rag_prompt | model | parser