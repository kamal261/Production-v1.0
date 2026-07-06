from collections import deque


class CrawlQueue:

    def __init__(self):

        self.queue = deque()
        self.visited = set()

    def push(self, url):

        if url in self.visited:
            return

        self.visited.add(url)
        self.queue.append(url)

    def pop(self):

        if not self.queue:
            return None

        return self.queue.popleft()

    def empty(self):

        return len(self.queue) == 0