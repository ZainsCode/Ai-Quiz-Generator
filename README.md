# 🤖 AI Quiz Generator

A beginner-friendly AI-powered quiz app built with Python, Streamlit, and Gemini.  
Just enter a topic — the app will generate multiple-choice questions, let you take the quiz, and score your performance!

## 🧠 Features

- ✅ Generate 4 multiple-choice questions on any topic
- ✅ View 4 options and select your answer
- ✅ See correct answers and your final score
- ✅ Clean browser-based interface (Streamlit)
- ✅ Beginner-friendly Python code structure


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-quiz-generator.git
cd ai-quiz-generator
```

2. Create and Activate Virtual Environment
Windows:
```
python -m venv venv
.\venv\Scripts\activate
```
Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
4. Install Dependencies
```
pip install -r requirements.txt
```
6. Add Your Gemini API Key
Create a .env file in the root directory:
GEMINI_KEY=your-api-key-here
You can get your API key from Gemini Api key Website

5. Run the App
streamlit run app.py
It will open automatically in your browser at http://localhost:8501.

🧰 Tech Stack
•	Python 3.10+ <br>
•	Streamlit – simple, fast GUI<br>
•	Gemini Api Key <br>
•	python-dotenv – load secret keys <br>

🗂️ Project Structure
ai-quiz-generator/ <br>
├── app.py               # Streamlit frontend <br>
├── quiz_generator.py    # AI logic using OpenAI API <br>
├── requirements.txt     # Python dependencies <br>
├── .env                 # Your OpenAI API key (do NOT upload to GitHub) <br>
└── .gitignore           # Ignore venv, .env, cache files <br>

🔐 Security
•	Your API key is stored in .env (never commit this file)
•	Make sure .env is ignore by using .gitignore


## 🙋‍♂️ Author
Zain Ali
Python & AI Developer — Building cool stuff

