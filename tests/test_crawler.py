from crawler.crawler import SiteCrawler


def test_crawler(browser):

    crawler = SiteCrawler(browser)

    pages = crawler.crawl("https://pooyamachine.com", limit=5)

    assert isinstance(pages, list)