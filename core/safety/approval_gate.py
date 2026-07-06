class ApprovalGate:

    def approve(self, action):

        dangerous = [
            "delete_post",
            "rewrite_all",
            "bulk_update"
        ]

        if action["type"] in dangerous:
            return False

        if action.get("confidence", 1) < 0.75:
            return False

        return True