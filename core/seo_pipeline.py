from seo.data.gsc_client import GSCClient
from seo.data.serp_api_client import SERPAPIClient
from seo.data.metrics_engine import MetricsEngine
from seo.data.data_normalizer import DataNormalizer

from seo.profit.keyword_value_engine import KeywordValueEngine

from seo.input.manual_config import ManualConfig

from seo.health.site_audit import SiteAudit
from seo.health.auto_fixer import AutoFixer
from core.config.env_loader import Env


class SEOPipeline:

    def __init__(self, llm_client, wp_client, your_domain, gsc_token, site_url, serp_api_key):

        self.llm = llm_client
        self.wp = wp_client
        self.domain = your_domain

        self.manual = ManualConfig()
        self.manual.seed()
        self.gsc = GSCClient(Env.GSC_TOKEN, Env.SITE_URL)
        self.serp = SERPAPIClient(Env.SERP_API_KEY)

        self.metrics = MetricsEngine()
        self.normalizer = DataNormalizer()

        self.value_engine = KeywordValueEngine()

        self.site_audit = SiteAudit()
        self.auto_fixer = AutoFixer(wp_client, llm_client)

    def run_data_cycle(self, start_date, end_date):

        gsc_raw = self.gsc.query(start_date, end_date)
        gsc_data = self.metrics.normalize_gsc(gsc_raw)

        enriched = {}

        for row in gsc_data:
            serp = self.serp.search(row["keyword"])
            enriched[row["keyword"]] = serp

        dataset = self.normalizer.merge(gsc_data, enriched)

        return dataset

    def evaluate_keywords(self, dataset):

        results = []

        for k, v in dataset.items():

            gsc = v["gsc"]

            serp = v["serp"]

            evaluation = self.value_engine.evaluate(
                k,
                serp.get("organic_results", []),
                {
                    "impressions": gsc["impressions"],
                    "ctr": gsc["ctr"],
                    "position": gsc["position"]
                }
            )

            results.append(evaluation)

        return results

    def run_site_audit(self, pages):

        return [self.site_audit.run(page) for page in pages]

    def auto_fix(self, pages, post_ids):

        for page, post_id in zip(pages, post_ids):

            audit = self.site_audit.run(page)

            self.auto_fixer.fix(
                post_id,
                audit["actions"],
                page
            )