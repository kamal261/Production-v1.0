class SERPFormatter:

    def format(self, raw_data):

        return {
            "query": raw_data.get("search_parameters", {}).get("q"),
            "organic_results": [
                {
                    "title": r.get("title"),
                    "link": r.get("link"),
                    "snippet": r.get("snippet")
                }
                for r in raw_data.get("organic_results", [])
            ]
        }