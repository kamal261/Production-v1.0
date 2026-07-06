class EvaluationHistory:

    def __init__(self):

        self.snapshots = []

    def add(self, snapshot):

        self.snapshots.append(snapshot)

    def last(self):

        return self.snapshots[-1] if self.snapshots else None