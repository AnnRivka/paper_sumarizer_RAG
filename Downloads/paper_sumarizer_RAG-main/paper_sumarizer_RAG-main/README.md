# Academic Paper Summarizer using RAG

This project was developed as part of the Intel® Unnati Industrial Training Program (Gen AI for Gen Z).

## Overview
This project demonstrates a functional Retrieval-Augmented Generation (RAG) pipeline for summarizing academic papers. Instead of passing the full document to a language model, the system performs document chunking, vector-based retrieval, and explicit context compression before summarization.

## Pipeline
1. Load academic document
2. Chunk the document into smaller sections
3. Create vector embeddings using TF-IDF
4. Retrieve relevant chunks using cosine similarity
5. Compress retrieved context
6. Generate final summary

## Project Structure


## How to Run
```bash
pip install -r requirements.txt
python app.py