import streamlit as st
from summarizer import summarize

st.set_page_config(page_title="Academic Paper Summarizer", layout="centered")

st.title("📄 Academic Paper Summarizer")
st.write("Intel® Unnati – GenAI Challenge (RAG & Context Compression Demo)")

paper_text = st.text_area(
    "Paste academic paper text here:",
    height=200,
    placeholder="Paste a few paragraphs from an academic paper..."
)

if st.button("Summarize"):
    if paper_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        summary = summarize(paper_text)
        st.subheader("🔎 Summary Output")
        st.success(summary)
