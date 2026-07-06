class CompetitorStrategy:

    def suggest_gaps(self, gaps):

        return [
            {"action": "create_content", "keyword": g}
            for g in gaps
        ]