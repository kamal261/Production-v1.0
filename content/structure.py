class ContentStructure:

    def build_outline(self, keyword):

        return {
            "h1": keyword,
            "h2": ["intro", "benefits", "faq"]
        }