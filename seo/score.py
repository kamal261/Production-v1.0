class SEOScore:

    def calculate(self, issues):

        score = 100

        penalties = {
            "MISSING_TITLE": 20,
            "MISSING_META_DESCRIPTION": 15,
            "MISSING_HEADINGS": 10,
            "THIN_CONTENT": 25
        }

        for i in issues:

            score -= penalties.get(i, 5)

        return max(score, 0)