class AIProviderError(Exception):
    """Base exception for AI providers."""
    pass


class AuthenticationError(AIProviderError):
    """Raised when API authentication fails."""
    pass


class APIConnectionError(AIProviderError):
    """Raised when the AI service cannot be reached."""
    pass


class AIResponseError(AIProviderError):
    """Raised when the AI returns an invalid response."""
    pass
