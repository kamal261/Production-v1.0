import requests


class SERPAPIClient:

    def __init__(self, api_key):

        self.api_key = api_key

    def search(self, keyword):

        url = "https://serpapi.com/search"

        params = {
            "q": keyword,
            "api_key": self.api_key
        }

        r = requests.get(url, params=params)
        return r.json()