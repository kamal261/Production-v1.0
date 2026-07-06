from providers.message import Message


class PromptBuilder:

    def __init__(self):

        self.messages = []

    def system(self, text):

        self.messages.append(
            Message.system(text)
        )

        return self

    def user(self, text):

        self.messages.append(
            Message.user(text)
        )

        return self

    def assistant(self, text):

        self.messages.append(
            Message.assistant(text)
        )

        return self

    def build(self):

        return self.messages