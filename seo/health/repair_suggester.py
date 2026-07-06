class RepairSuggester:

    def suggest(self, issues):

        actions = []

        for issue in issues:

            if issue == "MISSING_TITLE":

                actions.append({
                    "type": "update_title",
                    "method": "ai_generate"
                })

            elif issue == "MISSING_H1":

                actions.append({
                    "type": "add_h1",
                    "method": "ai_generate"
                })

            elif issue == "THIN_CONTENT":

                actions.append({
                    "type": "rewrite_content",
                    "method": "ai_generate"
                })

            elif isinstance(issue, dict) and issue["type"] == "BROKEN_LINKS":

                actions.append({
                    "type": "fix_links",
                    "method": "auto_replace"
                })

        return actions