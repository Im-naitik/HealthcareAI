from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import traceback
import os

from backend.chatbot import healthcare_chatbot
from backend.report_summarizer import summarize_report

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Healthcare Assistant API is running"}

@app.post("/chat")
def chat(query: str):
    response = healthcare_chatbot(query)
    return {"response": response}

@app.post("/summarize-report")
def summarize_pdf(file: UploadFile = File(...)):
    try:
        file_path = f"temp_{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        summary = summarize_report(file_path)

        os.remove(file_path)

        return {"summary": summary}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "traceback": traceback.format_exc()
            }
        )