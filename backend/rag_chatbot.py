from langchain_groq import ChatGroq
from backend.rag import search_medical_knowledge
from backend.safety import check_emergency
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.2)

def rag_healthcare_chat(user_query):
    if check_emergency(user_query):
        return "This may be urgent. Please contact emergency services or visit a hospital immediately."

    context = search_medical_knowledge(user_query)

    prompt = f"""
You are an AI Healthcare Assistant.

Use the context below to answer safely.

Context:
{context}

User question:
{user_query}

Rules:
- Give general educational information only
- Do not diagnose
- Do not prescribe medicine
- Recommend consulting a doctor
"""

    response = llm.invoke(prompt)
    return response.content