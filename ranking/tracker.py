class RankingTracker:

    def __init__(self):

        self.history = {}

    def update(self, keyword, position):

        self.history.setdefault(keyword, []).append(position)

    def get_history(self, keyword):

        return self.history.get(keyword, [])