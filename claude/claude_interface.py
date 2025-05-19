import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_claude(system_prompt: str, user_prompt: str, max_tokens=1024):
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",  
        max_tokens=max_tokens,
        temperature=0,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.content[0].text
