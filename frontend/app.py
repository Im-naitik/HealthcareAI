import streamlit as st
import requests

st.set_page_config(page_title="AI Healthcare Assistant", layout="wide")

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
            "http://127.0.0.1:8000/chat",
            params={"query": query}
        )

        st.write(response.json()["response"])

if menu == "Medical Report Summarizer":
    st.subheader("Upload Medical Report PDF")

    file = st.file_uploader("Upload PDF", type=["pdf"])

    if file:
        files = {"file": file.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/summarize-report",
            files={"file": file}
        )

        st.write(response.json()["summary"])