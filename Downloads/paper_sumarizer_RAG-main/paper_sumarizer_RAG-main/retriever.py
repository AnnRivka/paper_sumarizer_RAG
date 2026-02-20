# retriever.py
"""
Similarity-based retrieval for RAG.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_top_k(query_vector, document_vectors, chunks, k=3):
    """
    Retrieve top-k most relevant chunks using cosine similarity.
    """
    similarities = cosine_similarity(query_vector, document_vectors)[0]
    top_k_indices = np.argsort(similarities)[-k:][::-1]
    return [chunks[i] for i in top_k_indices]