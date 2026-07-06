class SEOAnalyzer:

    def analyze(self, page):

        issues = []

        if not page.title:
            issues.append("MISSING_TITLE")

        if not page.meta_description:
            issues.append("MISSING_META_DESCRIPTION")

        if len(page.headings) == 0:
            issues.append("MISSING_HEADINGS")

        if len(page.html) < 1000:
            issues.append("THIN_CONTENT")

        return issues