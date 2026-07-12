from app.loaders.pdf_loader import load_pdf
from app.splitters.text_splitters import split_documents
from app.embeddings.huggingface_embeddings import embeddings
from app.vectorstores.faiss_store import create_vector_store
from app.chains.rag_chain import chain

documents = load_pdf("data/resume.pdf")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks, embeddings)

retriever = vector_store.as_retriever()

question = "What internships does Ishani have?"

results = retriever.invoke(question)

context = "\n\n".join(
    [doc.page_content for doc in results]
)

response = chain.invoke(
    {
        "context": context,
        "question": question
    }
)

print(response)