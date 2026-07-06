class MetricsEngine:

    def normalize_gsc(self, data):

        results = []

        for row in data.get("rows", []):

            results.append({
                "keyword": row["keys"][0],
                "page": row["keys"][1],
                "clicks": row.get("clicks", 0),
                "impressions": row.get("impressions", 0),
                "ctr": row.get("ctr", 0),
                "position": row.get("position", 0)
            })

        return results

    def keyword_value(self, row):

        return (
            row["impressions"] * 0.4 +
            (1 - row["ctr"]) * 300 +
            (10 - row["position"]) * 100
        )