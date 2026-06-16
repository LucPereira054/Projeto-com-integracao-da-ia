import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

client=Client(api_key=os.environ.get("GEMINI_API"))

response=client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Olá, você está funcionando?"
)

print(response.text)
