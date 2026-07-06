class ContentGapFinder:

    def find(self, my_keywords, competitor_keywords):

        return list(set(competitor_keywords) - set(my_keywords))