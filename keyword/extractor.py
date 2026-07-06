class KeywordExtractor:

    def extract_from_serp(self, serp_data):

        keywords = []

        for r in serp_data.get("organic_results", []):

            title = r.get("title", "")

            keywords.extend(title.lower().split())

        return list(set(keywords))