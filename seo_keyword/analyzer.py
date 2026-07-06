class KeywordAnalyzer:

    def classify_intent(self, keyword):

        keyword = keyword.lower()

        if any(x in keyword for x in ["buy", "price", "cheap"]):
            return "transactional"

        if any(x in keyword for x in ["how", "what", "why"]):
            return "informational"

        return "navigational"