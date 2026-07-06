class KeywordAnalyzer:

    def score(self, impressions, ctr, position):

        return (
            impressions * 0.4 +
            (1 - ctr) * 200 +
            (10 - position) * 50
        )