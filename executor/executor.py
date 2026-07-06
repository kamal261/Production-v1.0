class Executor:

    def __init__(self, registry):

        self.registry = registry

    def execute(self, plan):

        context = {}

        result = None

        for task in plan.all():

            if task.tool == "crawl_site":

                result = self.registry.run(
                    task.tool,
                    task.input["url"],
                    task.input["limit"]
                )

                context["pages"] = result

            elif task.tool == "seo_audit":

                result = self.registry.run(
                    task.tool,
                    context["pages"]
                )

                context["report"] = result

            else:

                result = self.registry.run(
                    task.tool,
                    **task.input
                )

        return context