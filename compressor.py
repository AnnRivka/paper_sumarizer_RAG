def compress_text(text, max_sentences=3):
    sentences = text.split(".")
    compressed = sentences[:max_sentences]
    return ".".join(compressed).strip()
