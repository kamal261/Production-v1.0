class SEOReport:

    def build(self, page, issues, score):

        return {
            "url": page.url,
            "score": score,
            "issues": issues
        }