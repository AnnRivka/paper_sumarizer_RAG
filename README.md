# Academic Paper Summarizer using RAG

This project is an AI-powered academic paper summarizer built using Retrieval Augmented Generation (RAG) and context compression.

## Features
- Summarizes long academic papers
- Uses retrieval instead of full-context prompting
- Compresses context to reduce token usage
- Beginner-friendly implementation

## How it Works
1. Paper text is chunked into smaller parts
2. Relevant chunks are retrieved
3. Retrieved content is compressed
4. Compressed context is summarized using an LLM

## Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace Embeddings

## Creative / Unique Feature

This project includes a multi-level summarization approach:
- Short summary for quick understanding
- Detailed summary for deeper insight
- Bullet-point highlights for key takeaways

This feature allows users to control the level of detail while maintaining low token usage through context compression.

## Token Optimization
Instead of sending the entire academic paper to the model, only relevant and compressed sections are used. This significantly reduces token usage and latency.

## Creative Feature
The system supports multi-level summarization:
- Short overview
- Detailed summary
- Bullet-point highlights

This allows users to control verbosity while keeping token usage low.
