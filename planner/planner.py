from planner.plan import Plan
from planner.task import Task


class Planner:

    def build_site_audit(self, url):

        plan = Plan()

        plan.add(
            Task(
                tool="crawl_site",
                input={
                    "url": url,
                    "limit": 100
                }
            )
        )

        plan.add(
            Task(
                tool="seo_audit",
                input={}
            )
        )

        return plan