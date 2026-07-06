import time


class Cache:

    def __init__(self):

        self.store = {}

    def set(self, key, value, ttl=300):

        self.store[key] = {
            "value": value,
            "expire": time.time() + ttl
        }

    def get(self, key):

        item = self.store.get(key)

        if not item:
            return None

        if time.time() > item["expire"]:
            del self.store[key]
            return None

        return item["value"]