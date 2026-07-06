class Tool:

    name = "base"
    description = ""

    def run(self, *args, **kwargs):
        raise NotImplementedError