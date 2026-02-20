# compressor.py
"""
Context compression module.
Reduces retrieved chunks before passing them to the LLM.
"""

def compress_chunks(chunks, max_sentences=2):
    """
    Compress each chunk by keeping only the first few sentences.
    This reduces token usage while preserving key information.
    """
    compressed_chunks = []

    for chunk in chunks:
        sentences = chunk.split(".")
        compressed = ".".join(sentences[:max_sentences]).strip()
        compressed_chunks.append(compressed)

    return compressed_chunks