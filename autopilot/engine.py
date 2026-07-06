class AutoPilot:

    def decide(self, report):

        actions = []

        for r in report:

            if r["score"] < 50:

                actions.append({
                    "action": "fix_content",
                    "url": r["url"]
                })

        return actions