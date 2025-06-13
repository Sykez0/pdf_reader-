import os
from pdf_utils import extract_text_from_pdf, chunk_text
from rag_engine import embed_chunks
from qa_engine import answer_question

#1. Load PDF and chunk it
pdf_path = "sample.pdf"
text = extract_text_from_pdf(pdf_path)
print(f"📄 Type of extracted text: {type(text)}")
print(f"📄 Raw text preview: {text[:300]}")

chunks = chunk_text(text)

print(f"✅ Extracted {len(chunks)} chunks.")
print("🧠 Embedding and storing in ChromaDB...")

#2. Embed chunks and store in ChromaDB
vectordb = embed_chunks(chunks)
print("✅ Embeddings saved successfully.")

#3. Ask a question using local RAG + Ollama
print("\n💬 Ask a question about the PDF:")
question = input("❓> ")
response = answer_question(question, vectordb)

print("\n🤖 Answer:")
print(response)