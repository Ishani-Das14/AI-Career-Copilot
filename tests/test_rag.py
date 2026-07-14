from app.loaders.pdf_loader import load_pdf
from app.splitters.text_splitters import split_documents

documents = load_pdf("data/resume.pdf")

chunks = split_documents(documents)

print("=" * 50)
print("Chunk 3")
print("=" * 50)
print(chunks[3].page_content)

print("\nMetadata:")
print(chunks[3].metadata)