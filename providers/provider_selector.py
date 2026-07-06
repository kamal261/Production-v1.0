from core.config.env_loader import Env

from providers.factory import ProviderFactory


class ProviderSelector:

    def __init__(self):

        self.factory = ProviderFactory()

    def default(self):

        if Env.OPENAI_API_KEY:
            return self.factory.create("openai")

        if Env.OPENROUTER_API_KEY:
            return self.factory.create("openrouter")

        return self.factory.create("ollama")