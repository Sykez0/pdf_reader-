from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM as Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def load_vectorstore(persist_directory="db"):
    """Load the existing Chroma vector DB."""
    return Chroma(persist_directory=persist_directory)

def build_qa_chain(vectordb):
    """Set up a QA chain using local Ollama (Mistral) + the vector retriever."""
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    #OPTIONAL: Can adjust the prompt
    template = """Use the following context to answer the question:
    {context}

    Question: {question}
    Answer:"""
    prompt = PromptTemplate.from_template(template)

    llm = Ollama(model="mistral")

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )

    return chain

def answer_question(question, vectordb):
    """Ask a question and return the answer from the local model."""
    qa_chain = build_qa_chain(vectordb)
    return qa_chain.invoke({"query": question})
