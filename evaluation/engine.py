class EvaluationEngine:

    def evaluate_seo_report(self, report):

        results = {

            "total_pages": len(report),

            "avg_score": 0,

            "critical_issues": 0,

            "warnings": 0

        }

        if not report:
            return results

        total_score = 0

        for r in report:

            total_score += r.get("score", 0)

            for i in r.get("issues", []):

                if i in ["MISSING_TITLE", "MISSING_META_DESCRIPTION"]:
                    results["critical_issues"] += 1

                else:
                    results["warnings"] += 1

        results["avg_score"] = total_score / len(report)

        return results