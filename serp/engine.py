import requests

from core.config.env_loader import Env


class SERPEngine:

    def __init__(self):

        self.api_key = Env.SERP_API_KEY

        self.base_url = "https://serpapi.com/search.json"

    def search(self, query, num=10):

        if not self.api_key:
            raise ValueError("Missing SERP API key")

        params = {

            "q": query,

            "api_key": self.api_key,

            "num": num
        }

        response = requests.get(self.base_url, params=params, timeout=30)

        response.raise_for_status()

        return response.json()

    def extract_organic(self, data):

        results = []

        for item in data.get("organic_results", []):

            results.append({

                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet")
            })

        return results