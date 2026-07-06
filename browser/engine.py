from playwright.sync_api import sync_playwright

from core.constants import DEFAULT_TIMEOUT


class BrowserEngine:

    def __init__(self, headless=True):

        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )

        self.context = self.browser.new_context()

    def fetch_html(self, url):

        page = self.context.new_page()

        page.goto(url, timeout=DEFAULT_TIMEOUT * 1000)

        html = page.content()

        page.close()

        return html

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()