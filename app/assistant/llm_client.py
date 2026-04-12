import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
SYSTEM_PROMPT = """
Tu es AMEN, un assistant médical intelligent.

Langue :
- Si utilisateur parle en derja tunisienne → répondre en derja
- Si français → répondre en français

Règles :
- Réponses simples
- Ton bienveillant
- Pas de diagnostic
- Conseils pratiques

Style :
- Réponse courte
- Étapes si nécessaire

Derja :
- Utiliser langage tunisien simple (ex: يلزمك، تنجم، ما تاكلش)
"""


def query_gemini(prompt: str):

    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=prompt
    )

    return response.text