class AutoRunner:

    def run(self, actions):

        executed = []

        for a in actions:

            executed.append({

                "action": a,

                "status": "queued"

            })

        return executed