class SEOContentSync:

    def sync(self, client, post_id, data):

        return client.update_post(post_id, data)