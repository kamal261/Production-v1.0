from providers.prompt_builder import PromptBuilder


class ContentGenerator:

    def __init__(self, provider):

        self.provider = provider

    def generate(self, keyword, context):

        prompt = PromptBuilder() \
            .system("You are an SEO content writer") \
            .user(f"Write SEO content for: {keyword}") \
            .user(f"Context: {context}") \
            .build()

        return self.provider.chat(prompt)