# app.py
"""
End-to-end Academic Paper Summarizer using RAG + Compression.
"""

from embeddings import load_document, chunk_text, create_embeddings
from retriever import retrieve_top_k
from compressor import compress_chunks
from summarizer import summarize


def main():
    # 1. Load document
    text = load_document("data/sample_paper.txt")

    # 2. Chunk document
    chunks = chunk_text(text)

    # 3. Create embeddings
    doc_vectors, vectorizer = create_embeddings(chunks)

    # 4. Query
    query = "main contribution of the paper"
    query_vector = vectorizer.transform([query])

    # 5. Retrieve relevant chunks
    top_chunks = retrieve_top_k(query_vector, doc_vectors, chunks, k=2)

    print("\n--- Retrieved Chunks ---\n")
    for c in top_chunks:
        print(c[:300], "\n")

    # 6. Compress context
    compressed_chunks = compress_chunks(top_chunks, max_sentences=1)

    print("\n--- Compressed Context ---\n")
    for c in compressed_chunks:
        print(c, "\n")

    # 7. Final summarization
    final_context = " ".join(compressed_chunks)
    summary = summarize(final_context)

    print("\n=== FINAL SUMMARY ===\n")
    print(summary)


if __name__ == "__main__":
    main()