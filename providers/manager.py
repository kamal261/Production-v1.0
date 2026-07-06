from providers.openai_provider import OpenAIProvider
from providers.openrouter_provider import OpenRouterProvider
from providers.ollama_provider import OllamaProvider


class ProviderManager:

    def __init__(self):

        self.providers = {
            "openai": OpenAIProvider(),
            "openrouter": OpenRouterProvider(),
            "ollama": OllamaProvider()
        }

    def get(self, name):

        if name not in self.providers:
            raise ValueError(f"Unknown provider: {name}")

        return self.providers[name]