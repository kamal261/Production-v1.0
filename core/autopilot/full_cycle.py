class FullCycle:

    def __init__(self, pipeline, autopilot, tracker):

        self.pipeline = pipeline
        self.autopilot = autopilot
        self.tracker = tracker
        self.history = {}

    def run(self, keyword, pages):

        dataset = self.pipeline.run_data_cycle(None, None)

        actions = self.generate_actions(dataset)

        results = []

        for action in actions:

            results.append(self.autopilot.run_action(action))

        ranking = self.tracker.get_rank_snapshot(
            keyword,
            self.pipeline.domain
        )

        self.history[keyword] = ranking

        return {
            "keyword": keyword,
            "ranking": ranking,
            "actions": results
        }

    def generate_actions(self, dataset):

        actions = []

        for k, v in dataset.items():

            if v["gsc"]["ctr"] < 0.02:

                actions.append({
                    "type": "rewrite_content",
                    "post_id": k,
                    "confidence": 0.8
                })

        return actions