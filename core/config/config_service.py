from core.config.config_store import ConfigStore


class ConfigService:

    def __init__(self):

        self.store = ConfigStore()

    def get(self):

        return self.store.load()

    def set(self, key, value):

        data = self.store.load()

        data[key] = value

        self.store.save(data)

    def all(self):

        return self.store.load()