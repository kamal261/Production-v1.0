class BackupManager:

    def __init__(self, wp_client):

        self.wp = wp_client
        self.backups = {}

    def backup_post(self, post_id):

        data = self.wp.get_posts()
        self.backups[post_id] = data

        return True

    def restore(self, post_id):

        return self.backups.get(post_id, None)