class ComparisonEngine:

    def compare_scores(self, before, after):

        return {

            "improved": after["avg_score"] > before["avg_score"],

            "delta": after["avg_score"] - before["avg_score"]

        }