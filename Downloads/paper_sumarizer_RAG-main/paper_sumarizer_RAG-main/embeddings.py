# embeddings.py
"""
This module handles:
1. Reading academic text
2. Chunking the document
3. Creating vector embeddings using TF-IDF

This avoids raw LLM dependency and demonstrates real preprocessing logic.
"""

from sklearn.feature_extraction.text import TfidfVectorizer


def load_document(file_path: str) -> str:
    """
    Reads a text document from disk.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def chunk_text(text: str, chunk_size: int = 300) -> list:
    """
    Splits text into smaller chunks of fixed word length.
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def create_embeddings(chunks: list):
    """
    Converts text chunks into numerical vectors using TF-IDF.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    embeddings = vectorizer.fit_transform(chunks)

    return embeddings, vectorizer