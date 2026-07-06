from seo.profit.difficulty_estimator import DifficultyEstimator
from seo.profit.roi_scorer import ROIScorer


class KeywordValueEngine:

    def __init__(self):

        self.difficulty = DifficultyEstimator()
        self.roi = ROIScorer()

    def evaluate(self, keyword, serp_results, keyword_data):

        diff = self.difficulty.estimate(serp_results)

        value = self.roi.score(keyword_data, diff)

        return {
            "keyword": keyword,
            "difficulty": diff,
            "value_score": value,
            "priority": self._priority(value)
        }

    def _priority(self, value):

        if value > 1000:
            return "HIGH"
        elif value > 500:
            return "MEDIUM"
        return "LOW"