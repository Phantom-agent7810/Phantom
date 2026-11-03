import os
from dotenv import load_dotenv

from ai.provider import AIProvider
from ai.client import HTTPClient

load_dotenv()


class GeminiProvider(AIProvider):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = HTTPClient()

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        self.model = "gemini-flash-latest"

        self.url = (
            f"{self.base_url}/models/{self.model}:generateContent"
        )

    def generate(self, prompt: str) -> str:
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = self.client.post(
            url=self.url,
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": self.api_key,
            },
            json=payload,
        )

        return response["candidates"][0]["content"]["parts"][0]["text"]
