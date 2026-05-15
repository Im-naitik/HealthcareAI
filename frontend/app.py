import streamlit as st
import requests

st.set_page_config(page_title="AI Healthcare Assistant", layout="wide")

# Backend API URL
API_URL = "http://127.0.0.1:8000"

st.title("AI Healthcare Assistant")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Chatbot", "Medical Report Summarizer"]
)

if menu == "Chatbot":
    st.subheader("Ask Health Questions")

    query = st.text_area("Enter your question")

    if st.button("Ask AI"):

        response = requests.post(
            f"{API_URL}/chat",
            params={"query": query}
        )

        st.write(response.json()["response"])

if menu == "Medical Report Summarizer":
    st.subheader("Upload Medical Report PDF")

    file = st.file_uploader("Upload PDF", type=["pdf"])

    if file:

        files = {
        "file": (file.name, file.getvalue(), "application/pdf")
        }

        response = requests.post(
            f"{API_URL}/summarize-report",
            files=files
        )

        if response.status_code == 200:
            st.write(response.json()["summary"])
        else:
            st.error("Backend Error")
            st.code(response.text)