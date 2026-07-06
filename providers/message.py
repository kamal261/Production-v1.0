class Message:

    @staticmethod
    def system(text):

        return {
            "role": "system",
            "content": text
        }

    @staticmethod
    def user(text):

        return {
            "role": "user",
            "content": text
        }

    @staticmethod
    def assistant(text):

        return {
            "role": "assistant",
            "content": text
        }