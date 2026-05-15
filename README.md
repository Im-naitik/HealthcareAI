# HealthcareAI

HealthcareAI is an advanced AI-powered healthcare assistant that combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), FastAPI, Streamlit, and vector databases to provide intelligent healthcare support.

The project allows users to:
- Chat with an AI healthcare assistant
- Upload and summarize medical reports
- Retrieve healthcare-related information using RAG
- Process PDFs and medical documents
- Interact through a modern frontend interface

This project is designed to demonstrate practical AI engineering, backend development, NLP pipelines, and healthcare-focused GenAI applications.

---

# Features

## AI Healthcare Chatbot
An intelligent healthcare chatbot capable of answering healthcare-related queries using LLMs and Retrieval-Augmented Generation.

## Medical Report Summarization
Upload medical PDF reports and generate concise AI-powered summaries.

## Retrieval-Augmented Generation (RAG)
Uses vector embeddings and FAISS vector databases for context-aware responses.

## FastAPI Backend
Scalable REST API backend built using FastAPI.

## Streamlit Frontend
Interactive user interface built with Streamlit.

## Vector Database Integration
Uses FAISS for efficient semantic search and retrieval.

## PDF Processing
Extracts and processes text from uploaded medical reports.

## Modular Architecture
Clean and scalable project structure for future improvements and deployment.

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI / NLP
- LangChain
- FAISS
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)

## Frontend
- Streamlit

## PDF Processing
- PyMuPDF
- PDF Text Extraction

## Environment & Utilities
- dotenv
- requests

---

# Project Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── Healthcare Chatbot
  ├── PDF Report Summarizer
  ├── RAG Pipeline
  └── Vector Database
          │
          ▼
        FAISS
          │
          ▼
        LLM API
```

---

# Project Structure

```bash
HealthcareAI/
│
├── backend/
│   ├── main.py
│   ├── chatbot.py
│   ├── report_summarizer.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   └── utils.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── medical_docs/
│
├── uploads/
│
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Im-naitik/HealthcareAI.git
```

---

## 2. Navigate to Project Directory

```bash
cd HealthcareAI
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

---

# Running the Application

## Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

Open a new terminal and run:

```bash
streamlit run frontend/app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# API Endpoints

# Home Endpoint

```http
GET /
```

### Response

```json
{
  "message": "AI Healthcare Assistant API is running"
}
```

---

# Chat Endpoint

```http
POST /chat
```

### Parameters

| Parameter | Type | Description |
|----------|------|-------------|
| query | string | User healthcare query |

### Example Request

```http
POST /chat?query=What are the symptoms of diabetes?
```

---

# PDF Summarization Endpoint

```http
POST /summarize-pdf
```

### Upload
- Medical PDF Report

### Output
- AI-generated summary of the uploaded report

---

# How RAG Works in This Project

1. Medical documents are processed and converted into embeddings.
2. Embeddings are stored in the FAISS vector database.
3. User queries are converted into embeddings.
4. Relevant medical context is retrieved from FAISS.
5. Retrieved context is sent to the LLM.
6. LLM generates accurate and context-aware responses.

---

# Future Improvements

- Medical Image Classification
- X-ray Analysis using CNNs
- Pneumonia Detection
- Skin Disease Classification
- Voice-Based AI Assistant
- Multi-Language Support
- Electronic Health Record Integration
- Appointment Recommendation System
- Cloud Deployment
- Docker Support
- Authentication System
- Chat History Storage
- AI Agent Workflow Integration

---

# Use Cases

- AI Healthcare Assistance
- Medical Report Analysis
- Healthcare Chatbot Systems
- GenAI Healthcare Applications
- Medical Information Retrieval
- NLP Research Projects
- AI/ML Portfolio Projects

---

# Learning Outcomes

This project demonstrates knowledge of:

- FastAPI Backend Development
- LangChain Framework
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Databases
- LLM Integration
- Streamlit Frontend Development
- PDF Processing
- AI Application Development
- REST API Design
- NLP Pipelines

---

# Requirements

Example dependencies:

```txt
fastapi
uvicorn
streamlit
langchain
faiss-cpu
python-dotenv
pymupdf
requests
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Screenshots

Add your project screenshots here.

Example:

```md
![Home Page](images/home.png)
![Chatbot](images/chatbot.png)
![PDF Summary](images/summary.png)
```

---

# Deployment

You can deploy this project using:

- Render
- Railway
- Streamlit Cloud
- Hugging Face Spaces
- AWS
- Google Cloud Platform
- Azure

---

# Author

Naitik Katiyar

GitHub:
https://github.com/Im-naitik

LinkedIn:
https://www.linkedin.com/in/katiyar-naitik/

---

# License

This project is licensed under the MIT License.

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Make changes
4. Commit changes
5. Push to your branch
6. Open a Pull Request

---

# Acknowledgements

- LangChain
- FastAPI
- Streamlit
- FAISS
- Groq
- Open Source AI Community
