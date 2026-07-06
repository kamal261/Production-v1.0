import base64
from core.config.env_loader import Env


class WPAuth:

    def __init__(self):

        token = f"{Env.WP_USERNAME}:{Env.WP_APP_PASSWORD}"

        self.headers = {
            "Authorization": "Basic " +
            base64.b64encode(token.encode()).decode()
        }