class KeywordEngine:

    def __init__(self):

        self.keywords = []

    def add(self, keyword):

        if keyword not in self.keywords:
            self.keywords.append(keyword)

    def all(self):

        return self.keywords