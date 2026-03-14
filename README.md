# 🤖 AI Resume Interviewer

An AI-powered application that analyzes a resume and generates technical interview questions, answers, and resume insights using a local LLM.

This project allows users to upload their resume and interact with it using AI.

---

## 🚀 Features

• Upload Resume (PDF)  
• AI-generated Resume Summary  
• Technical Interview Questions with Answers  
• Chat with your Resume  
• Runs on Local LLM (No API cost)

---

## 🧠 Tech Stack

- Python
- Streamlit
- Ollama
- Llama3 (Local LLM)
- PDFPlumber

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. The system extracts the resume content
3. AI analyzes the resume using a local LLM
4. The application generates:

- Resume summary
- Interview questions with answers
- AI chatbot responses based on the resume

---

## 🖥️ Demo Flow

Upload Resume → AI Analysis → Questions + Answers → Resume Chatbot

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-resume-interviewer.git
cd ai-resume-interviewer

---

## 📂 Project Structure

ai-resume-interviewer/
- │── app.py              # Main Streamlit application
- │── backend.ipynb       # Backend logic / experiments
- │── requirements.txt    # Dependencies

---

## 🔮 Future Improvements

- **The following features are planned for future versions of this project:**

- **Skill Extraction from Resume**  
  Automatically detect and list technical skills from the uploaded resume.

- **AI Mock Interview Mode**  
  Simulate a real interview where the AI asks questions and evaluates the candidate's responses.

- **Resume Scoring System**  
  Analyze the resume and provide a score based on structure, skills, and experience.

- **Resume Improvement Suggestions**  
  Provide AI-driven recommendations to improve the resume for better job opportunities.

- **RAG-based Resume Chatbot**  
  Implement Retrieval-Augmented Generation (RAG) so users can ask questions and get answers strictly based on their resume content.

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vikash029/ai-resume-interviewer.git
   cd ai-resume-interviewer
2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the Streamlit app**
   ```bash
   streamlit run app.py

---


## 📖 Usage
1. Open the app in your browser (default: http://localhost:8501)
2. Upload your resume (PDF format)
3. Get AI-generated interview questions and suggested answers
4. Practice and prepare confidently!

## 🌐 Expose App Publicly with ngrok
If you want to share your Streamlit app over the internet, you can use **ngrok**:

1. **Install ngrok**
   - Download from [ngrok.com](https://ngrok.com/download)
   - Or install via Homebrew (Mac):
     ```bash
     brew install ngrok/ngrok/ngrok
     ```

2. **Authenticate ngrok**
   - Sign up at [ngrok.com](https://ngrok.com) and get your auth token.
   - Run:
     ```bash
     ngrok config add-authtoken <YOUR_AUTH_TOKEN>
     ```

3. **Run your Streamlit app**
   ```bash
   streamlit run app.py
   ```






