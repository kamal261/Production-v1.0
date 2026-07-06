class AutoExecutor:

    def run(self, actions, wordpress_client):

        results = []

        for a in actions:

            if a["action"] == "fix_content":

                results.append({
                    "url": a["url"],
                    "status": "queued"
                })

        return results