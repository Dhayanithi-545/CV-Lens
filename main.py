import streamlit as st
import PyPDF2
import io
import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Page config
st.set_page_config(page_title="CV Lens", page_icon="📄", layout="centered")

# Title
st.title("CV Lens - AI Resume Critiquer")
st.markdown("Upload your resume and get AI powered feedback tailored to your needs")

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# File uploader & role input
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")
analyze = st.button("Analyze Resume")

# Function: Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function: Extract text from file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# Function: Query OpenRouter
def query_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 1000,
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    return response.json()

# Handle resume analysis
if analyze:
    try:
        if not uploaded_file:
            st.error("Please upload a resume first.")
            st.stop()

        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content bro...")
            st.stop()

        # Create prompt
        prompt = f"""
        Please analyze this resume and provide constructive feedback.

        Focus on:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        5. Give a score out of 100, and tell it would be better if it is greater than 80

        Resume content:
        {file_content}

        Provide your analysis in a clear, structured format with specific recommendations.
        If everything is good, highlight strengths as encouragement.
        """

        # Call OpenRouter API
        response = query_openrouter(prompt)

        # Extract result safely
        result_text = response["choices"][0]["message"]["content"]

        # Show results
        st.markdown("### 📊 Analysis Results")
        st.markdown(result_text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer credits
st.markdown("---")
# Footer credits with custom CSS
st.markdown(
    """
    <style>
        .footer {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            font-size: 15px;
            color: #333;
            margin-top: 30px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.08);
        }
        .footer a {
            text-decoration: none;
            color: #0066cc;
            font-weight: 500;
        }
        .footer a:hover {
            color: #ff4b4b;
        }
    </style>

    <div class="footer">
        <b>Built with ❤️ by Dhayanithi</b><br>
        🔗 <a href="https://dhayanithi.vercel.app" target="_blank">Portfolio</a> | 
        💼 <a href="https://www.linkedin.com/in/dhayanithi-anandan-69199a322/" target="_blank">LinkedIn</a> | 
        📸 <a href="https://www.instagram.com/dhaya_545/" target="_blank">Instagram</a> | 
        🖥️ <a href="https://github.com/Dhayanithi-545" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

