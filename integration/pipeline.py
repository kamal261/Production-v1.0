class Pipeline:

    def __init__(self, executor, evaluation_engine):

        self.executor = executor
        self.evaluation_engine = evaluation_engine

    def run(self, plan):

        result = self.executor.execute(plan)

        evaluation = self.evaluation_engine.evaluate_seo_report(
            result.get("report", [])
        )

        return {
            "execution": result,
            "evaluation": evaluation
        }