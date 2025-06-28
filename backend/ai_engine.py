from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the key
client = OpenAI(api_key=api_key)

def match_bible_verse(input_text):
    prompt = f"""
You are a Bible assistant.

User input:
"{input_text}"

Respond with the most relevant Bible verse (reference and verse text in KJV, King James Version). Do not explain.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a Bible assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
