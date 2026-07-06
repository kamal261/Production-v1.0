class DryRun:

    def __init__(self):

        self.enabled = True

    def execute(self, action, wp_client):

        if self.enabled:

            return {
                "status": "DRY_RUN",
                "action": action
            }

        return wp_client.update_post(
            action["post_id"],
            action["data"]
        )