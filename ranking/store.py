class RankingStore:

    def __init__(self):

        self.data = {}

    def save(self, keyword, position):

        self.data.setdefault(keyword, []).append(position)

    def get(self, keyword):

        return self.data.get(keyword, [])