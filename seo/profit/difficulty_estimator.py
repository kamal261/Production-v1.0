class DataNormalizer:

    def merge(self, gsc_data, serp_data):

        merged = {}

        for row in gsc_data:

            key = row["keyword"]

            merged[key] = {
                "gsc": row,
                "serp": serp_data.get(key, {})
            }

        return merged