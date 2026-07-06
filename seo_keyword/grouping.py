class KeywordGrouping:

    def group(self, keywords):

        groups = {}

        for kw in keywords:

            key = kw[0].lower()

            groups.setdefault(key, []).append(kw)

        return groups