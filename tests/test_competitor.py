from competitor.engine import CompetitorEngine


def test_competitor():

    c = CompetitorEngine()

    result = c.extract({"organic_results": []})

    assert isinstance(result, list)