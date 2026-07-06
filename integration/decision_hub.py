class DecisionHub:

    def __init__(self, decision_engine):

        self.engine = decision_engine

    def process(self, evaluation, rankings):

        return self.engine.decide(evaluation, rankings)