class ROIScorer:

    def score(self, keyword_data, difficulty):

        impressions = keyword_data.get("impressions", 100)
        ctr = keyword_data.get("ctr", 0.02)
        position = keyword_data.get("position", 10)

        value = (
            impressions * 0.5 +
            (1 - ctr) * 200 +
            (10 - difficulty) * 100 +
            (10 - position) * 50
        )

        return value