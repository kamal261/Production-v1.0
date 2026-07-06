class RiskEngine:

    def evaluate(self, action):

        risk = 0

        if action["type"] == "update_title":
            risk += 10

        if action["type"] == "rewrite_content":
            risk += 50

        if action.get("content_length", 0) > 2000:
            risk += 20

        return {
            "risk_score": risk,
            "safe": risk < 40
        }