from langchain_groq import ChatGroq
from backend.safety import check_emergency
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)

def healthcare_chatbot(user_query):
    if check_emergency(user_query):
        return """
This may be a medical emergency. Please contact emergency services or visit the nearest hospital immediately.
I cannot diagnose or treat emergency conditions.
"""

    prompt = f"""
You are an AI Healthcare Assistant.
Give general health information only.
Do not provide final diagnosis.
Always recommend consulting a licensed doctor.

User question:
{user_query}
"""

    response = llm.invoke(prompt)
    return response.content