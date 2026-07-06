class IntentDetector:

    def detect(self, keyword):

        if "how" in keyword:
            return "informational"

        if "buy" in keyword:
            return "transactional"

        return "navigational"