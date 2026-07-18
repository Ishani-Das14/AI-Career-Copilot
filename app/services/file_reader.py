from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def read_document(file_path):
    """
    Read text from supported document types.

    Supported:
    - PDF (.pdf)
    - Text (.txt)
    """

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    # Read PDF
    if extension == ".pdf":
        loader = PyPDFLoader(str(file_path))
        documents = loader.load()

        text = "\n".join(
            document.page_content
            for document in documents
        )

        return text

    # Read TXT
    elif extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    else:
        raise ValueError(f"Unsupported file type: {extension}")