class DecisionEngine:

    def decide(self, evaluation, rankings):

        actions = []

        if evaluation["avg_score"] < 60:

            actions.append("SEO_REWRITE")

        if evaluation["critical_issues"] > 0:

            actions.append("FIX_CRITICAL_ISSUES")

        if rankings.get("trend") == "down":

            actions.append("CONTENT_BOOST")

        return actions