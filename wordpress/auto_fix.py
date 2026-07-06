class AutoFixEngine:

    def apply(self, page, fixes):

        if "title" in fixes:
            page.title = fixes["title"]

        if "content" in fixes:
            page.html = fixes["content"]

        return page