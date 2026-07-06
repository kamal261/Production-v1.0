from urllib.parse import urljoin
from bs4 import BeautifulSoup

from crawler.page import Page
from crawler.queue import CrawlQueue


class SiteCrawler:

    def __init__(self, browser):

        self.browser = browser
        self.queue = CrawlQueue()
        self.pages = []

    def crawl(self, start_url, limit=50):

        self.queue.push(start_url)

        while not self.queue.empty():

            if len(self.pages) >= limit:
                break

            url = self.queue.pop()

            html = self.browser.fetch_html(url)

            page = self.parse(url, html)

            self.pages.append(page)

            for link in page.links:
                self.queue.push(link)

        return self.pages

    def parse(self, url, html):

        soup = BeautifulSoup(html, "html.parser")

        page = Page(url=url, html=html)

        page.title = soup.title.text.strip() if soup.title else ""

        page.links = [
            urljoin(url, a["href"])
            for a in soup.find_all("a", href=True)
        ]

        page.headings = [
            h.text.strip()
            for h in soup.find_all(["h1", "h2"])
        ]

        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            page.meta_description = meta.get("content", "")

        return page