class WPPublisher:

    def __init__(self, client):

        self.client = client

    def publish_update(self, post_id, title, content):

        return self.client.update_post(
            post_id,
            {
                "title": title,
                "content": content
            }
        )