from google import genai
from google.genai import types

# Initialize client with API key
client = genai.Client(api_key=API_key)

def generate_quiz(topic):
    prompt = (
        f"Generate 4 multiple-choice quiz questions about '{topic}'. "
        "Each question should have 1 correct answer and 3 wrong answers. "
        "Format like this:\n"
        "Question: ...\n"
        "A. ...\n"
        "B. ...\n"
        "C. ...\n"
        "D. ...\n"
        "Correct Answer: ...\n\n"
        "Do not include explanations."
    )

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=prompt  # or types.Part.from_text(text=prompt)
    )

    return response.text
