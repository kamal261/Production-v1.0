class FeedbackLoop:

    def __init__(self, comparison_engine):

        self.comparison = comparison_engine

    def analyze(self, before, after):

        return self.comparison.compare_scores(before, after)