import requests

from core.config.env_loader import Env

from providers.base import BaseProvider


class OpenRouterProvider(BaseProvider):

    name = "openrouter"

    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    def chat(self, messages, **kwargs):

        response = requests.post(

            self.BASE_URL,

            headers={

                "Authorization": f"Bearer {Env.OPENROUTER_API_KEY}",

                "Content-Type": "application/json"

            },

            json={

                "model": kwargs.get(
                    "model",
                    Env.DEFAULT_MODEL
                ),

                "messages": messages,

                "temperature": kwargs.get(
                    "temperature",
                    0.2
                )

            },

            timeout=60

        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]