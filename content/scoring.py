class ContentScoring:

    def score(self, content):

        length_score = min(len(content) / 10, 100)

        keyword_score = 50 if "SEO" in content else 20

        return (length_score + keyword_score) / 2