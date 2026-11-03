from ai.provider import AIProvider


class GroqProvider(AIProvider):
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Groq provider is not implemented yet.")
