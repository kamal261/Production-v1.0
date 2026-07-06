import requests

from core.config.env_loader import Env

from providers.base import BaseProvider


class OllamaProvider(BaseProvider):

    name = "ollama"

    def chat(self, messages, **kwargs):

        response = requests.post(

            f"{Env.OLLAMA_URL}/api/chat",

            json={

                "model": kwargs.get(
                    "model",
                    "llama3"
                ),

                "messages": messages,

                "stream": False

            },

            timeout=120

        )

        response.raise_for_status()

        return response.json()["message"]["content"]