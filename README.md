# 🧠 Chat with PDF – Retrieval-Augmented Generation Demo

A simple end-to-end RAG (Retrieval-Augmented Generation) pipeline built in **Python + LlamaIndex + OpenAI**.

It loads any PDF, cleans and chunks the text, builds embeddings, stores them in a temporary in-memory vector index, and lets you ask natural-language questions about the content.

---

## 🚀 Features
- 📄 PDF ingestion and text cleaning  
- 🔢 Embedding creation via OpenAI  
- 🔍 Semantic retrieval using LlamaIndex `VectorStoreIndex`  
- 💬 Question-Answer interface with OpenAI LLM  
- 📊 Optional 2-D visualization of embeddings (PCA)

---

## 🧰 Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/g0utham-a/chat-with-pdf.git
cd chat-with-pdf
