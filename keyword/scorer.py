class KeywordScorer:

    def score(self, volume, difficulty, ctr):

        return (volume * 0.5) - (difficulty * 0.3) + (ctr * 0.2)