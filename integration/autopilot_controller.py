class AutoPilotController:

    def __init__(self, runner):

        self.runner = runner

    def execute(self, actions):

        return self.runner.run(actions)