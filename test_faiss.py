from app.loaders.pdf_loader import load_pdf
from app.splitters.text_splitters import split_documents
from app.embeddings.huggingface_embeddings import embeddings
from app.vectorstores.faiss_store import create_vector_store

# Load PDF
documents = load_pdf("data/resume.pdf")

# Split into chunks
chunks = split_documents(documents)

# Create vector store
vector_store = create_vector_store(chunks, embeddings)

print(type(vector_store))

retriever = vector_store.as_retriever()

print(type(retriever))

# Search
results = retriever.invoke(
    "What internships does Ishani have?"
)

print(f"\nResults Found: {len(results)}")

print("\nFirst Result:\n")
print(results[0].page_content)
