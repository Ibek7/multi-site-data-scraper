import unittest
from scrapers.academic.pubmed_scraper import scrape_pubmed

class TestPubMedScraper(unittest.TestCase):
    def test_scrape_pubmed(self):
        self.assertIsNone(scrape_pubmed("machine learning"))