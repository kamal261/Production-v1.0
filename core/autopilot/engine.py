from core.safety.dry_run import DryRun
from core.safety.backup_manager import BackupManager
from core.safety.approval_gate import ApprovalGate
from core.safety.risk_engine import RiskEngine


class SEOAutopilot:

    def __init__(self, wp_client):

        self.wp = wp_client
        self.dry_run = DryRun()
        self.backup = BackupManager(wp_client)
        self.approval = ApprovalGate()
        self.risk = RiskEngine()

    def run_action(self, action):

        risk = self.risk.evaluate(action)

        if not risk["safe"]:
            return {"status": "BLOCKED", "reason": "HIGH_RISK"}

        if not self.approval.approve(action):
            return {"status": "BLOCKED", "reason": "NOT_APPROVED"}

        self.backup.backup_post(action["post_id"])

        return self.dry_run.execute(action, self.wp)