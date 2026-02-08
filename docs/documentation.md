# Project Documentation

## Problem Statement
Academic research papers are often long and difficult to understand quickly. Processing entire papers using large language models is expensive and inefficient.

## Proposed Solution
This project implements an Academic Paper Summarizer using Retrieval Augmented Generation (RAG) combined with context compression to efficiently summarize papers while reducing token usage.

## System Workflow
1. Load academic paper text
2. Split the text into smaller chunks
3. Retrieve relevant chunks
4. Compress retrieved context
5. Generate a concise summary using an LLM

## Context Compression Strategy
Instead of sending the full document to the model, only the most relevant and compressed information is passed, significantly reducing token consumption.

## Benefits
- Faster summarization
- Reduced API cost
- Scalable to large documents
- Beginner-friendly design
