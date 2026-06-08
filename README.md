# Document-Intelligence-System
An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to interact with large PDF documents through natural language questions. The system extracts text from PDFs, generates semantic embeddings using Hugging Face Sentence Transformers, stores document vectors in FAISS, retrieves relevant context for user queries, and leverages Google Gemini to generate accurate, context-aware responses.

## Features

* PDF text extraction using PyMuPDF
* Semantic text chunking and embedding generation
* Vector similarity search using FAISS
* Context-aware answer generation with Google Gemini
* Persistent vector index and metadata storage
* Interactive command-line chatbot interface
* Source-grounded responses to reduce hallucinations

## Tech Stack

* Python
* FAISS
* Hugging Face Sentence Transformers
* Google Gemini API
* PyMuPDF

## Architecture

PDF Document → Text Extraction → Chunking → Embeddings → FAISS Vector Store → Retrieval → Gemini → Answer Generation

## Example Questions

* Who is the main character?
* What prophecy was given to Kali?
* Describe the relationship between two characters.
* Summarize a specific chapter or event.

This project demonstrates the implementation of a production-style RAG pipeline for document question answering and knowledge retrieval over long-form content.
