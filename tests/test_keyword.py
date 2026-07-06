from seo_keyword.engine import KeywordEngine


def test_keywords():

    k = KeywordEngine()

    k.add("seo")

    assert "seo" in k.all()