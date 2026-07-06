from urllib.parse import urlparse


class URLUtils:

    def domain(self, url):

        return urlparse(url).netloc

    def normalize(self, url):

        return url.rstrip("/")