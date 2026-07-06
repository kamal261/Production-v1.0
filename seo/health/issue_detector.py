class IssueDetector:

    def detect(self, page, broken_links):

        issues = []

        if not page.title:
            issues.append("MISSING_TITLE")

        if not getattr(page, "headings", []):
            issues.append("MISSING_H1")

        if broken_links:
            issues.append({
                "type": "BROKEN_LINKS",
                "count": len(broken_links)
            })

        if len(page.html) < 1000:
            issues.append("THIN_CONTENT")

        return issues