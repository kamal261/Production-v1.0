import requests
from core.config.env_loader import Env
from wordpress.auth import WPAuth


class WordPressClient:

    def __init__(self):

        self.base = Env.WP_SITE.rstrip("/")
        self.auth = WPAuth()

    def get_posts(self):

        url = f"{self.base}/wp-json/wp/v2/posts"

        r = requests.get(url, headers=self.auth.headers)

        return r.json()

    def update_post(self, post_id, data):

        url = f"{self.base}/wp-json/wp/v2/posts/{post_id}"

        r = requests.post(url, json=data, headers=self.auth.headers)

        return r.json()