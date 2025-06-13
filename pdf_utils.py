import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            try:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            except Exception as e:
                print(f"⚠️ Failed to extract text from a page: {e}")
    return text.strip() or " "  # Avoid returning None or empty


def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    """
    Splits text into chunks for processing.
    Each chunk is 1000 characters long with an overlap of 200 characters.
    This is useful for processing large texts in manageable pieces.
    Args:
        text (str): The text to be split into chunks.
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The overlap between chunks.

    Returns:
        list: A list of text chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_text(text)