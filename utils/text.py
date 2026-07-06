class TextUtils:

    def clean(self, text):

        return text.strip().lower()

    def truncate(self, text, length=160):

        return text[:length]