# summarizer.py
"""
Final summarization module.
This module ONLY handles generation, not retrieval or compression.
"""

def summarize(context: str) -> str:
    """
    Simple extractive-style summarizer (non-LLM placeholder).
    This keeps the project fully runnable without API keys.
    """
    sentences = context.split(".")
    return ". ".join(sentences[:3]).strip()