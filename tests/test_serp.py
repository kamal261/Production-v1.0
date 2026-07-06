from serp.engine import SERPEngine


def test_serp():

    serp = SERPEngine()

    data = serp.search("seo test")

    assert "organic_results" in data