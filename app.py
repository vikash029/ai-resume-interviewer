import streamlit as st
import pdfplumber
import ollama

st.set_page_config(page_title="AI Resume Interviewer", layout="wide")

st.title("🤖 AI Resume Interviewer + Resume Chat")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

# -------- Extract Resume --------
@st.cache_data
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


if uploaded_file:

    if "resume_text" not in st.session_state:
        st.session_state.resume_text = extract_text(uploaded_file)

    # ⚡ limit resume size for faster AI response
    text = st.session_state.resume_text[:3000]

    st.success("✅ Resume uploaded successfully!")

    col1, col2 = st.columns(2)

    # -------- Resume Summary --------
    with col1:
        if st.button("📄 Generate Resume Summary"):
            prompt = f"""
            Summarize the following resume in 5 clear bullet points.

            Resume:
            {text}
            """
            with st.spinner("Analyzing resume..."):
                response = ollama.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": prompt}]
                )
            st.session_state["resume_summary"] = response["message"]["content"]

        if "resume_summary" in st.session_state:
            st.subheader("📄 Resume Summary")
            st.write(st.session_state["resume_summary"])

    # -------- Interview Questions --------
    with col2:
        if st.button("🎯 Generate Interview Questions"):
            prompt = f"""
            You are a senior technical interviewer.

            Based on the resume below generate 10 technical interview
            questions with answers.

            Resume:
            {text}

            Format:

            Question:
            Answer:
            """
            with st.spinner("Generating interview questions..."):
                response = ollama.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": prompt}]
                )
            st.session_state["interview_questions"] = response["message"]["content"]

        if "interview_questions" in st.session_state:
            st.subheader("🎯 Interview Questions & Answers")
            st.write(st.session_state["interview_questions"])

    # -------- Resume Chat --------
    st.divider()
    st.subheader("💬 Chat with your Resume")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Ask something about your resume")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        prompt = f"""
        You are an AI career assistant.

        Answer the user's question using the resume context.

        Resume:
        {text}

        Question:
        {user_input}
        """
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

        ai_response = response["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # -------- Show Chat History --------
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])
