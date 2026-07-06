class CompetitorMetrics:

    def compute_overlap(self, my_keywords, competitor_keywords):

        return len(set(my_keywords) & set(competitor_keywords))