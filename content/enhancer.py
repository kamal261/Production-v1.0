class ContentEnhancer:

    def enhance(self, content, suggestions):

        return content + "\n\n" + "\n".join(suggestions)