from tools.base import Tool


class BrowserTool(Tool):

    name = "browser_fetch"
    description = "Fetch HTML using browser engine"

    def __init__(self, browser_engine):

        self.browser = browser_engine

    def run(self, url):

        return self.browser.fetch_html(url)