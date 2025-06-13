from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def embed_chunks(chunks, persist_directory="db"):
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    vectordb.persist()
    return vectordb

