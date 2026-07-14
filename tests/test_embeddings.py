from app.loaders.pdf_loader import load_pdf
from app.splitters.text_splitters import split_documents
from app.embeddings.huggingface_embeddings import embeddings

documents = load_pdf("data/resume.pdf")

chunks = split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

vector = embeddings.embed_query(chunks[0].page_content)

print(f"Embedding Dimension: {len(vector)}")

print("\nFirst 10 Values:")
print(vector[:10])

print("\nChunk Preview:")
print(chunks[0].page_content[:200])