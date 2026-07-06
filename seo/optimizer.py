class SEOOptimizer:

    def suggest(self, issues):

        actions = []

        for issue in issues:

            if issue == "MISSING_TITLE":

                actions.append({
                    "type": "update_title"
                })

            if issue == "MISSING_META_DESCRIPTION":

                actions.append({
                    "type": "update_meta_description"
                })

            if issue == "THIN_CONTENT":

                actions.append({
                    "type": "rewrite_content"
                })

        return actions