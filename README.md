# HealthcareAI

AI-powered healthcare assistant built using FastAPI, Streamlit, Generative AI, and Deep Learning.  
This project combines conversational healthcare support, medical report summarization and chest X-ray pneumonia detection in a single platform.

## Features

### AI Healthcare Chatbot
- Conversational healthcare assistant
- Answers health-related questions using LLMs
- Built using FastAPI and Generative AI APIs

### Medical Report Summarizer
- Upload PDF medical reports
- Extracts and summarizes report content
- Helps users quickly understand medical documents

### Chest X-ray Pneumonia Detection
- CNN-based medical image classification
- Detects Pneumonia vs Normal chest X-rays
- Built using TensorFlow/Keras

### Streamlit Frontend
- Interactive web interface
- Upload reports and X-ray images
- Chat with AI assistant in real time

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI / Machine Learning
- TensorFlow
- Keras
- CNN
- Generative AI APIs

## Frontend
- Streamlit

## Other Libraries
- NumPy
- Pillow
- PyMuPDF
- Requests

---

# Project Structure

```bash
HealthcareAI/
│
├── backend/
│   ├── main.py
│   ├── chatbot.py
│   ├── report_summarizer.py
│   │
│   └── image_model/
│       ├── train_cnn.py
│       ├── predict_xray.py
│       └── xray_model.h5
│
├── frontend/
│   └── app.py
│
├── notebooks/
│   └── xray_training.ipynb
│
├── data/
│   └── chest_xray/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Im-naitik/HealthcareAI.git

cd HealthcareAI
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Dataset

Dataset used for X-ray classification:

Chest X-Ray Images (Pneumonia)

Download dataset from Kaggle and place it inside:

```bash
data/chest_xray/
```

Dataset structure:

```bash
data/chest_xray/
│
├── train/
├── val/
└── test/
```

---

# Train CNN Model

Run:

```bash
python backend/image_model/train_cnn.py
```

Or use:

```bash
notebooks/xray_training.ipynb
```

The trained model will be saved as:

```bash
backend/image_model/xray_model.h5
```

---

# Run FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

API documentation:

```bash
http://127.0.0.1:8000/docs
```

---

# Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs at:

```bash
http://localhost:8501
```

---

# API Endpoints

## Chatbot

```bash
POST /chat
```

## Medical Report Summarizer

```bash
POST /summarize-report
```

## X-ray Prediction

```bash
POST /predict-xray
```

---

# Future Improvements

- Transfer Learning using ResNet50 / EfficientNet
- Grad-CAM heatmap visualization
- Multi-disease X-ray classification
- Docker deployment
- AWS deployment
- Authentication system
- RAG-based medical knowledge retrieval
- Medical voice assistant

---

# Deployment

The project can be deployed using:

- AWS EC2
- Render
- Docker
- Streamlit Cloud

---

# Author

Naitik Katiyar

GitHub: https://github.com/Im-naitik

Portfolio: https://im-naitik.github.io/portfolio/

LinkedIn: https://www.linkedin.com/in/katiyar-naitik/
