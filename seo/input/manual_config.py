from seo.input.keyword_store import KeywordStore
from seo.input.competitor_store import CompetitorStore


class ManualConfig:

    def __init__(self):
         self.keywords = KeywordStore()
         self.competitors = CompetitorStore()

    def seed(self):

        self.keywords.bulk_add([
            "seo agent",
            "wordpress seo",
            "content optimization",
            "ai seo tool"
        ])

        self.competitors.bulk_add([
            "ahrefs.com",
            "semrush.com",
            "moz.com"
        ])

    def get_state(self):

        return {
            "keywords": self.keywords.get_all(),
            "competitors": self.competitors.get_all()
        }