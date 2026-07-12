from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI Resume Assistant.

    Answer the user's question only using the provided context.

    If the answer is not present in the context, say:
    "I couldn't find that information in the provided resume."

    Context:
    {context}

    Question:
    {question}
    """
)