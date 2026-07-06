from tools.base import Tool


class CrawlTool(Tool):

    name = "crawl_site"
    description = "Crawl website pages"

    def __init__(self, crawler):

        self.crawler = crawler

    def run(self, start_url, limit=50):

        return self.crawler.crawl(start_url, limit)