import fitz
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)

def extract_text_from_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def summarize_report(pdf_path):
    report_text = extract_text_from_pdf(pdf_path)

    if not report_text.strip():
        return "No readable text found in this PDF."

    prompt = f"""
You are a medical report explanation assistant.

Explain this medical report in simple language:
{report_text[:6000]}

Include:
1. Key findings
2. Normal/abnormal values
3. Possible meaning
4. What questions the patient should ask a doctor

Do not give diagnosis.
"""

    response = llm.invoke(prompt)
    return response.content