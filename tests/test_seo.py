from seo.analyzer import SEOAnalyzer


def test_seo():

    analyzer = SEOAnalyzer()

    page = type("P", (), {
        "title": "",
        "meta_description": "",
        "headings": [],
        "html": ""
    })

    issues = analyzer.analyze(page)

    assert isinstance(issues, list)