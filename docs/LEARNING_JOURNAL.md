# Commit 3 - Prompt Templates & LCEL

## Learned
- ChatPromptTemplate
- LCEL
- Dynamic placeholders

## Implemented
- Created reusable prompt
- Built first LCEL chain

## Key Takeaway
Prompt Templates + LCEL make AI pipelines modular.

# Commit 4 - Output Parser

## Learned
- StrOutputParser
- AIMessage vs String

## Implemented
- Added parser to LCEL pipeline

## Key Takeaway
Output Parsers simplify model responses.

# Commit 5 - ATS Resume Matcher

## Learned
- Multiple Prompt Variables
- Prompt Engineering
- File Handling

## Implemented
- Built ATS Resume Matcher
- Added file reader service
- Moved inputs to external files

## Key Takeaway
Separated data, business logic, and AI logic.

# Commit 6 - PDF Loading & Text Splitting

## Learned
- PyPDFLoader
- LangChain Documents
- RecursiveCharacterTextSplitter
- Chunking & Overlap

## Implemented
- Added PDF loader
- Created reusable text splitter
- Loaded resume PDF
- Split documents into chunks

## Key Takeaway
Documents must be split into smaller chunks before creating embeddings for RAG.

---

# Commit 7 - Embeddings & Retrieval

## Learned
- Hugging Face Embeddings
- Vector Embeddings
- FAISS
- Retriever
- Semantic Search

## Implemented
- Added Hugging Face embeddings
- Built FAISS vector store
- Created semantic retriever
- Retrieved relevant resume chunks


## Key Takeaway
RAG retrieves relevant document chunks using vector similarity before sending context to the LLM.