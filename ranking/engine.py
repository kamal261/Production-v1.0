class RankingEngine:

    def trend(self, history):

        if len(history) < 2:
            return "stable"

        if history[-1] < history[-2]:
            return "improving"

        if history[-1] > history[-2]:
            return "declining"

        return "stable"