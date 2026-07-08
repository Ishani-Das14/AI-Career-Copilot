from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly AI tutor."),
        ("human", "{question}")
    ]
)