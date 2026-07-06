class WPFixer:

    def apply_fixes(self, page, actions):

        fixes = {}

        for a in actions:

            if a["type"] == "update_title":
                fixes["title"] = page.title + " (SEO)"

            if a["type"] == "rewrite_content":
                fixes["content"] = page.html

        return fixes