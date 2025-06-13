Author: Brayden Moore (Aka Sykez)

Sunshot Research Lite is a lightweight, privacy-focused AI research assistant that helps users extract and interact with insights from academic PDFs — all running entirely on your local machine. This tool eliminates the need for cloud APIs, ensuring your documents stay private and secure.

The system uses HuggingFace embeddings to process PDF content into meaningful vector representations, which are then stored in ChromaDB. A local large language model (LLM), such as Mistral via Ollama, powers the question-answering functionality. To make the experience more accessible, the app includes both a command-line interface and an interactive Streamlit-based user interface.

To get started, clone the repository using git clone, navigate into the project directory, and set up a virtual environment. On Windows, you can activate it using .\venv\Scripts\activate, and on Mac or Linux with source venv/bin/activate. Install the required dependencies with pip install -r requirements.txt.

The app can be launched either by running python app.py for the CLI version, or streamlit run app_streamlit.py to open the web-based interface at http://localhost:8501. If you're using a local model like Mistral, ensure that Ollama is installed and you’ve downloaded the model with ollama run mistral.

Internally, the project is structured into modules that handle PDF extraction, chunking, embedding, vector storage, and question-answering logic. All of this is wrapped in a friendly user experience with Streamlit.

This tool is ideal for students, researchers, and developers who want to explore and summarize dense documents without relying on external services. It's also a solid base for building more advanced RAG (Retrieval-Augmented Generation) pipelines or AI reading assistants.

Future development plans include support for multiple PDFs, advanced semantic search over a local document library, in-line citation highlights, and exporting summaries to Markdown or Notion. Sunshot Research Lite is open-source under the MIT License and proudly developed by Brayden Moore, a Computer Science student at Wilfrid Laurier University.

If you'd like to see the original CLI file structure, streamlit interface, or even contribute, visit the project repository and check out the full documentation and source code
