import sys
import os

# Let this file find your backend code
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from backend.services.ingestion import parse_pdf
from backend.utils.chunker import chunk_text
from backend.services.retrieval import store_chunks, search
from backend.services.llm import generate_answer


# ---------- Page setup ----------
st.set_page_config(page_title="Document Intelligence", page_icon="📄", layout="wide")

st.title("📄 Document Intelligence Platform")
st.caption("Upload documents and ask questions — answers grounded in your sources.")


# ---------- Sidebar: upload ----------
with st.sidebar:
    st.header("Documents")

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        if st.button("Process document"):
            with st.spinner("Reading, chunking, and storing..."):
                # Save the uploaded file temporarily
                temp_path = f"/tmp/{uploaded_file.name}"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Reuse your existing pipeline
                text = parse_pdf(temp_path)
                chunks = chunk_text(text)
                count = store_chunks(chunks)

            st.success(f"Stored {count} chunks from {uploaded_file.name}")


# ---------- Main area: ask ----------
question = st.text_input("Ask a question about your documents")

if question:
    with st.spinner("Searching and generating answer..."):
        relevant_chunks = search(question)
        answer = generate_answer(question, relevant_chunks)

    # Show the answer in a highlighted box
    st.subheader("Answer")
    st.info(answer)

    # Show the source chunks used
    st.subheader("Sources used")
    for i, chunk in enumerate(relevant_chunks):
        with st.expander(f"Source chunk {i + 1}"):
            st.write(chunk)