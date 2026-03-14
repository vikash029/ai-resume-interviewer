# AI Resume Interviewer

Upload your resume and generate **AI-based interview questions and answers** to prepare for interviews more effectively.

---

## 🚀 Features
- Upload resume in PDF format
- Automatically generate interview questions based on your resume
- AI-powered answers using Llama3 via Ollama
- Simple and interactive UI with Streamlit

---

## 🛠 Tech Stack
- **Python** – Core programming language
- **Streamlit** – Web app framework
- **Ollama** – Model serving
- **Llama3** – Large Language Model for Q&A

---

## 📂 Project Structure

ai-resume-interviewer/
- **│── app.py              # Main Streamlit application
- **│── backend.ipynb       # Backend logic / experiments
- **│── requirements.txt    # Dependencies


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






