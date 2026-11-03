import os
from dotenv import load_dotenv

from ai.provider import AIProvider
from ai.openrouter import OpenRouterProvider
from ai.gemini import GeminiProvider
from ai.groq import GroqProvider

load_dotenv()


class AIManager:
    def __init__(self, provider: AIProvider = None):
        if provider:
            self.provider = provider
            return

        provider_name = os.getenv("AI_PROVIDER", "openrouter").lower()

        if provider_name == "openrouter":
            self.provider = OpenRouterProvider()

        elif provider_name == "gemini":
            self.provider = GeminiProvider()

        elif provider_name == "groq":
            self.provider = GroqProvider()

        else:
            raise ValueError(f"Unknown AI provider: {provider_name}")

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
