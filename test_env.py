from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

if key:
    print("✅ API key loaded successfully!")
    print(f"Key starts with: {key[:8]}...")
else:
    print("❌ API key not found.")
