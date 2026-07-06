from providers.manager import ProviderManager


class ProviderFactory:

    def __init__(self):

        self.manager = ProviderManager()

    def create(self, provider_name):

        return self.manager.get(provider_name)