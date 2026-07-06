class TechnicalSEO:

    def check(self, page):

        return {
            "has_title": bool(page.title),
            "has_meta": bool(page.meta_description),
            "h1_count": len(page.headings),
            "html_size": len(page.html)
        }