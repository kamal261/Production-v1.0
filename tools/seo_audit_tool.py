from tools.base import Tool

from seo.analyzer import SEOAnalyzer
from seo.score import SEOScore
from seo.report import SEOReport


class SEOAuditTool(Tool):

    name = "seo_audit"

    description = "Analyze crawled pages"

    def __init__(self):

        self.analyzer = SEOAnalyzer()

        self.score = SEOScore()

        self.report = SEOReport()

    def run(self, pages):

        reports = []

        for page in pages:

            issues = self.analyzer.analyze(page)

            score = self.score.calculate(issues)

            reports.append(

                self.report.build(
                    page,
                    issues,
                    score
                )

            )

        return reports