# CV Lens - AI Resume Critiquer 📄

An intelligent resume analysis tool powered by AI that provides personalized feedback to help you improve your resume for specific job roles.

## ✨ Features

- **Multi-format Support**: Upload resumes in PDF or TXT format
- **AI-Powered Analysis**: Get detailed feedback using OpenAI's GPT-4o-mini model
- **Job-Specific Feedback**: Tailor analysis to specific job roles you're targeting
- **Comprehensive Review**: Covers content clarity, skills presentation, experience descriptions, and improvement suggestions
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- **Instant Results**: Get feedback within seconds of uploading your resume

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: OpenAI GPT-4o-mini (via OpenRouter API)
- **PDF Processing**: PyPDF2
- **Environment Management**: python-dotenv
- **HTTP Requests**: requests library

## 📋 Prerequisites

- Python 3.7 or higher
- OpenRouter API key (for accessing OpenAI models)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dhayanithi-545/cv-lens.git
   cd cv-lens
   ```

2. **Install required packages**
   ```bash
   pip install streamlit PyPDF2 requests python-dotenv
   ```

3. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

4. **Get your OpenRouter API Key**
   - Visit [OpenRouter](https://openrouter.ai/)
   - Sign up for an account
   - Generate an API key
   - Add it to your `.env` file

## 🏃‍♂️ Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Upload your resume**
   - Click "Browse files" and select your resume (PDF or TXT)
   - Optionally enter the job role you're targeting

3. **Get AI feedback**
   - Click "Analyze Resume"
   - Review the detailed feedback and recommendations

## 📊 What You'll Get

The AI analysis covers:

- **Content Clarity**: How clear and impactful your resume content is
- **Skills Presentation**: How well your skills are showcased
- **Experience Descriptions**: Quality of your work experience descriptions
- **Job-Specific Improvements**: Tailored suggestions for your target role
- **Strengths Highlighting**: Recognition of what you're doing well

## 📁 Project Structure

```
cv-lens/
│
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (not in repo)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Configuration

The application uses the following default settings:
- **Model**: OpenAI GPT-4o-mini
- **Temperature**: 0.7 (balanced creativity/consistency)
- **Max Tokens**: 1000 (comprehensive feedback)

You can modify these in the `query_openrouter()` function if needed.

## 📝 Requirements.txt

Create a `requirements.txt` file with:

```
streamlit
PyPDF2
requests
python-dotenv
```

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repo to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your `OPENROUTER_API_KEY` in the app secrets

### Local Network
```bash
streamlit run app.py --server.address 0.0.0.0
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dhayanithi Anandan**

- 🌐 [Portfolio](https://dhayanithi.vercel.app)
- 💼 [LinkedIn](https://www.linkedin.com/in/dhayanithi-anandan-69199a322/)
- 📸 [Instagram](https://www.instagram.com/dhaya_545/)
- 🖥️ [GitHub](https://github.com/Dhayanithi-545)

## 🙏 Acknowledgments

- OpenRouter for providing easy access to OpenAI models
- Streamlit for the amazing web framework
- PyPDF2 for PDF processing capabilities

## 🐛 Known Issues

- Large PDF files might take longer to process
- Complex formatting in PDFs may not be perfectly extracted

## 🔮 Future Enhancements

- Support for more file formats (DOCX, RTF)
- Resume scoring system
- ATS (Applicant Tracking System) compatibility check
- Resume template suggestions
- Multiple AI model options

---

⭐ If you find this project helpful, please give it a star on GitHub!