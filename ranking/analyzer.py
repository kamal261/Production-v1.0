class RankingAnalyzer:

    def trend(self, positions):

        if len(positions) < 2:
            return "stable"

        if positions[-1] < positions[-2]:
            return "up"

        if positions[-1] > positions[-2]:
            return "down"

        return "stable"