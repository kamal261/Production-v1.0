from openai import OpenAI

from core.config.env_loader import Env

from providers.base import BaseProvider


class OpenAIProvider(BaseProvider):

    name = "openai"

    def __init__(self):

        self.client = OpenAI(
            api_key=Env.OPENAI_API_KEY
        )

    def chat(self, messages, **kwargs):

        response = self.client.chat.completions.create(
            model=kwargs.get(
                "model",
                Env.DEFAULT_MODEL
            ),
            messages=messages,
            temperature=kwargs.get(
                "temperature",
                0.2
            )
        )

        return response.choices[0].message.content