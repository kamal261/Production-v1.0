from collections import deque


class Memory:

    def __init__(self, max_items=100):

        self.history = deque(maxlen=max_items)

    def add(self, item):

        self.history.append(item)

    def get(self):

        return list(self.history)

    def clear(self):

        self.history.clear()