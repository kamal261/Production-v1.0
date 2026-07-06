class KeywordFilter:

    def filter_stopwords(self, keywords):

        stopwords = {"the", "and", "is", "in", "on", "a", "to"}

        return [k for k in keywords if k not in stopwords]