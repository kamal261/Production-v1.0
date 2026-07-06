class CompetitorAnalyzer:

    def analyze(self, serp_results):

        competitors = []

        for r in serp_results.get("organic_results", []):

            link = r.get("link", "")

            competitors.append(link)

        return list(set(competitors))