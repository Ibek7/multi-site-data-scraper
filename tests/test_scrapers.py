import unittest
from scrapers.academic.pubmed_scraper import scrape_pubmed
from scrapers.news.bbc_scraper import scrape_bbc_africa
from scrapers.news.aljazeera_scraper import scrape_aljazeera_africa
from scrapers.news.guardian_scraper import scrape_guardian_global_development
from scrapers.academic.google_scholar_scraper import scrape_google_scholar
from scrapers.academic.ssrn_scraper import scrape_ssrn
from scrapers.news.reuters_scraper import scrape_reuters_africa 


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


class TestAlJazeeraScraper(unittest.TestCase):
    def test_scrape_aljazeera_africa(self):
        data = scrape_aljazeera_africa()
        self.assertIsNotNone(data, "Scraped data should not be None.")
        self.assertIsInstance(data, list, "Scraped data should be a list.")
        self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
        self.assertIn("title", data[0], "Each article should have a title.")
        self.assertIn("link", data[0], "Each article should have a link.")


class TestGuardianScraper(unittest.TestCase):
    def test_scrape_guardian_global_development(self):
        data = scrape_guardian_global_development()
        self.assertIsNotNone(data, "Scraped data should not be None.")
        self.assertIsInstance(data, list, "Scraped data should be a list.")
        self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
        self.assertIn("title", data[0], "Each article should have a title.")
        self.assertIn("link", data[0], "Each article should have a link.")



class TestGoogleScholarScraper(unittest.TestCase):
    def test_scrape_google_scholar(self):
        data = scrape_google_scholar(config_path="configs/academic.yaml")
        self.assertIsNotNone(data, "Scraped data should not be None.")
        self.assertIsInstance(data, list, "Scraped data should be a list.")
        self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
        self.assertIn("title", data[0], "Each article should have a title.")
        self.assertIn("authors", data[0], "Each article should have authors.")
        self.assertIn("link", data[0], "Each article should have a link.")


# class TestSSRNScraper(unittest.TestCase):
#     def test_scrape_ssrn(self):
#         data = scrape_ssrn("human trafficking")
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")



class TestReutersScraper(unittest.TestCase):
    def test_scrape_reuters_africa(self):
        data = scrape_reuters_africa()
        self.assertIsNotNone(data, "Scraped data should not be None.")
        self.assertIsInstance(data, list, "Scraped data should be a list.")
        self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
        self.assertIn("title", data[0], "Each article should have a title.")
        self.assertIn("link", data[0], "Each article should have a link.")
        self.assertIn("published_time", data[0], "Each article should have a published time.")