from compressor import compress_text

def summarize(text):
    compressed_text = compress_text(text)
    summary = f"Summary:\n{compressed_text}."
    return summary
