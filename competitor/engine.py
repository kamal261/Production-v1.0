class CompetitorEngine:

    def extract(self, serp_results):

        competitors = []

        for r in serp_results.get("organic_results", []):

            link = r.get("link")

            if link:

                competitors.append(link)

        return list(set(competitors))