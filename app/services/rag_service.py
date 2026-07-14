from app.loaders.pdf_loader import load_pdf
from app.splitters.text_splitters import split_documents
from app.embeddings.huggingface_embeddings import embeddings
from app.vectorstores.faiss_store import create_vector_store
from app.chains.rag_chain import chain


def create_retriever(pdf_path):

    documents = load_pdf(pdf_path)

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks, embeddings)

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 8
        }
    )

    return retriever


def retrieve_context(retriever, question):

    results = retriever.invoke(question)

    print("\n========== Retrieved Chunks ==========\n")

    for i, doc in enumerate(results, start=1):
        print(f"\n----- Chunk {i} -----\n")
        print(doc.page_content)

    context = "\n\n".join(
        doc.page_content for doc in results
    )

    return context


def ask_question(pdf_path, question):

    retriever = create_retriever(pdf_path)

    context = retrieve_context(
        retriever,
        question
    )

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response

