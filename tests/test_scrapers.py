import unittest
from scrapers.academic.pubmed_scraper import scrape_pubmed
from scrapers.news.bbc_scraper import scrape_bbc_africa
class TestPubMedScraper(unittest.TestCase):
    def test_scrape_pubmed(self):
        self.assertIsNone(scrape_pubmed("machine learning"))

class TestBBCScraper(unittest.TestCase):
    def test_scrape_bbc_africa(self):
        data = scrape_bbc_africa()
        self.assertIsNotNone(data, "Scraped data should not be None.")
        self.assertIsInstance(data, list, "Scraped data should be a list.")
        self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
        self.assertIn("title", data[0], "Each article should have a title.")
        self.assertIn("link", data[0], "Each article should have a link.")