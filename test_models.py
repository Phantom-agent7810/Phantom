import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"

response = requests.get(url)

print("Status:", response.status_code)
print(response.text)
