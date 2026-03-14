import streamlit as st
import pdfplumber
import ollama

st.title("AI Resume  10 Interviewer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    if st.button("Generate Questions"):

        prompt = f"""
        You are a senior technical interviewer.

        Analyze this resume and generate 10 technical interview questions WITH answers.

        Resume:
        {text}

        Return the output in this format:

        1. Question:

        == Answer:

        2. Question:

        == Answer:

        """

        with st.spinner("Generating interview questions..."):

            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

        st.subheader("Interview Questions & Answers")

        st.write(response["message"]["content"])