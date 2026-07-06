from browser.engine import BrowserEngine
from crawler.crawler import SiteCrawler
from planner.planner import Planner
from executor.executor import Executor
from tools.registry import ToolRegistry
from tools.crawl_tool import CrawlTool
from tools.seo_audit_tool import SEOAuditTool


class SEOAgent:
    def __init__(self):
        self.browser = None

        try:
            self.browser = BrowserEngine()
            self.browser.start()

            crawler = SiteCrawler(self.browser)

            registry = ToolRegistry()
            registry.register(CrawlTool(crawler))
            registry.register(SEOAuditTool())

            self.executor = Executor(registry)
            self.planner = Planner()

        except Exception:
            if self.browser:
                self.browser.close()
            raise

    def audit(self, url: str):
        plan = self.planner.build_site_audit(url)
        return self.executor.execute(plan)

    def close(self):
        if self.browser:
            self.browser.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()