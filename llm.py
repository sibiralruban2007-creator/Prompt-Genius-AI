
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def generate_response(prompt, temperature=0.7, max_tokens=500):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "Please add your Groq API key to your .env file."

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"