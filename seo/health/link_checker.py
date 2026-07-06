import requests
from bs4 import BeautifulSoup


class LinkChecker:

    def check(self, html, base_url):

        soup = BeautifulSoup(html, "html.parser")

        broken_links = []

        for a in soup.find_all("a", href=True):

            url = a["href"]

            try:

                r = requests.head(url, timeout=3)

                if r.status_code >= 400:
                    broken_links.append(url)

            except:
                broken_links.append(url)

        return broken_links