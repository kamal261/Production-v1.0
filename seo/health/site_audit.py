from seo.health.link_checker import LinkChecker
from seo.health.issue_detector import IssueDetector
from seo.health.repair_suggester import RepairSuggester


class SiteAudit:

    def __init__(self):

        self.link_checker = LinkChecker()
        self.detector = IssueDetector()
        self.suggester = RepairSuggester()

    def run(self, page):

        broken = self.link_checker.check(page.html, page.url)

        issues = self.detector.detect(page, broken)

        actions = self.suggester.suggest(issues)

        return {
            "url": page.url,
            "issues": issues,
            "actions": actions
        }