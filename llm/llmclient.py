import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # MUST be before os.getenv

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content


