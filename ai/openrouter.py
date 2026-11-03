import os
from dotenv import load_dotenv

from ai.provider import AIProvider
from ai.client import HTTPClient

load_dotenv()


class OpenRouterProvider(AIProvider):
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.client = HTTPClient()

        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found.")

        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def health_check(self) -> bool:
        return self.api_key is not None

    def generate(self, prompt: str) -> str:
        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        response = self.client.post(
            url=self.url,
            headers=headers,
            json=payload,
        )

        return response["choices"][0]["message"]["content"]
