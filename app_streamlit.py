import streamlit as st
from pdf_utils import extract_text_from_pdf, chunk_text
from rag_engine import embed_chunks
from qa_engine import answer_question
import tempfile
import os

st.title("🧠 SunShot: Local AI-Powered Research Assistant")

# Step 1: Upload PDF
uploaded_file = st.file_uploader("📄 Upload a research PDF", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_pdf_path = tmp_file.name

    # Step 2: Extract + chunk text
    text = extract_text_from_pdf(temp_pdf_path)
    chunks = chunk_text(text)

    st.success(f"✅ Extracted and chunked {len(chunks)} segments.")

    # Step 3: Embed chunks
    vectordb = embed_chunks(chunks)

    # Step 4: Ask question
    st.subheader("💬 Ask a question about the document")
    question = st.text_input("❓ Your question:")

    if question:
        with st.spinner("🤖 Thinking..."):
            response = answer_question(question, vectordb)
        st.markdown(f"**Answer:** {response}")
