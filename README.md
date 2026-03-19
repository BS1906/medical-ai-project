# 🧠 Medical AI Assistant (RAG System)

An end-to-end AI system that extracts information from medical reports and answers user queries using Generative AI.

## 🚀 Features
- PDF Upload → Google Cloud Storage
- Document AI for OCR extraction
- Smart text chunking
- Vertex AI Embeddings
- FAISS Vector Search
- Gemini LLM for answer generation

## 🧠 Architecture
PDF → Document AI → Chunking → Embeddings → Vector DB → Gemini → Answer

## 🛠 Tech Stack
- Python
- Google Cloud (Document AI, Vertex AI)
- FAISS
- Gemini API

🔑 Setup

Add your Gemini API key

Configure GCP credentials


---

## 🔐 IMPORTANT (DON’T FORGET)

Add `.gitignore`:

```text
.env
*.json
__pycache__/

## 📸 Example
Question: "Is the brain normal?"
Answer: "Yes, the CT scan is within normal limits."

## 🚀 How to Run
```bash
pip install -r requirements.txt
python document_ai_from_gcs.py