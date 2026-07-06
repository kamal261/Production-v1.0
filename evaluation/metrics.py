class MetricsEngine:

    def compute(self, evaluation):

        return {

            "health_score": evaluation["avg_score"],

            "issue_ratio": evaluation["critical_issues"] / max(1, evaluation["total_pages"]),

            "warning_ratio": evaluation["warnings"] / max(1, evaluation["total_pages"])

        }