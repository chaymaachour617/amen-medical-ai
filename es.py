import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def query_gemini(prompt: str):

    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=prompt
    )

    return response.text


print(query_gemini("Hello, how are you?"))