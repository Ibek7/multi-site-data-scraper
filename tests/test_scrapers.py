import unittest
from scrapers.academic.pubmed_scraper import scrape_pubmed
from scrapers.news.bbc_scraper import scrape_bbc_africa
from scrapers.news.aljazeera_scraper import scrape_aljazeera_africa
from scrapers.news.guardian_scraper import scrape_guardian_global_development
from scrapers.academic.google_scholar_scraper import scrape_google_scholar
from scrapers.academic.ssrn_scraper import scrape_ssrn
from scrapers.news.reuters_scraper import scrape_reuters_africa 
from scrapers.news.africanews_scraper import scrape_africanews
from scrapers.news.mail_guardian_scraper import scrape_mail_guardian
from scrapers.news.cnn_africa_scraper import scrape_cnn_africa
from scrapers.news.theeastafrican_scraper import scrape_theeastafrican 
from scrapers.news.un_news_africa_scraper import scrape_un_news_africa
from scrapers.news.daily_nation_scraper import scrape_daily_nation_specific
import urllib.parse


# class TestPubMedScraper(unittest.TestCase):
#     def test_scrape_pubmed(self):
#         self.assertIsNone(scrape_pubmed("machine learning"))

# class TestBBCScraper(unittest.TestCase):
#     def test_scrape_bbc_africa(self):
#         data = scrape_bbc_africa()
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")


# class TestAlJazeeraScraper(unittest.TestCase):
#     def test_scrape_aljazeera_africa(self):
#         data = scrape_aljazeera_africa()
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")


# class TestGuardianScraper(unittest.TestCase):
#     def test_scrape_guardian_global_development(self):
#         data = scrape_guardian_global_development()
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")



# class TestGoogleScholarScraper(unittest.TestCase):
#     def test_scrape_google_scholar(self):
#         data = scrape_google_scholar(config_path="configs/academic.yaml")
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("authors", data[0], "Each article should have authors.")
#         self.assertIn("link", data[0], "Each article should have a link.")

# ######
# class TestSSRNScraper(unittest.TestCase):
#     def test_scrape_ssrn(self):
#         data = scrape_ssrn("human trafficking")
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")



# class TestReutersScraper(unittest.TestCase):
#     def test_scrape_reuters_africa(self):
#         data = scrape_reuters_africa()
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")
#         self.assertIn("published_time", data[0], "Each article should have a published time.")

# #####
# class TestAfricaNewsScraper(unittest.TestCase):
#     def test_scrape_africanews(self):
#         data = scrape_africanews()
#         print("Scraped data:", data)  # Debugging output
#         self.assertIsNotNone(data, "Scraped data should not be None.")
#         self.assertIsInstance(data, list, "Scraped data should be a list.")
#         self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", data[0], "Each article should have a title.")
#         self.assertIn("link", data[0], "Each article should have a link.")



# class TestMailGuardianScraper(unittest.TestCase):
#     def test_scrape_mail_guardian_success(self):
#         articles = scrape_mail_guardian()
#         self.assertIsNotNone(articles, "Scraped data should not be None.")
#         self.assertIsInstance(articles, list, "Scraped data should be a list.")
#         self.assertGreater(len(articles), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", articles[0], "Each article should have a title.")
#         self.assertIn("link", articles[0], "Each article should have a link.")
        
#         # Added this to print scraped articles for debugging purposes
#         print("Scraped Articles:")
#         for article in articles:
#             print(f"Title: {article['title']}, Link: {article['link']}")



# class TestCNNAfricaScraper(unittest.TestCase):
#     def test_scrape_cnn_africa_success(self):
#         try:
#             articles = scrape_cnn_africa()
#             self.assertIsNotNone(articles, "Scraped data should not be None.")
#             self.assertIsInstance(articles, list, "Scraped data should be a list.")
#             self.assertGreater(len(articles), 0, "Scraped data should contain at least one article.")
#             for article in articles:
#                 self.assertIn("title", article, "Each article should have a title.")
#                 self.assertIn("link", article, "Each article should have a link.")
            
#             # Print scraped articles
#             print("\nScraped Articles:")
#             for article in articles:
#                 print(f"Title: {article['title']}, Link: {article['link']}")

#         except FileNotFoundError as e:
#             self.fail(f"FileNotFoundError: {e}")
#         except Exception as e:
#             self.fail(f"An unexpected error occurred: {e}")


# class TestTheEastAfricanScraper(unittest.TestCase):
#     def test_scrape_theeastafrican_success(self):
#         articles = scrape_theeastafrican()
#         self.assertIsNotNone(articles, "Scraped data should not be None.")
#         self.assertIsInstance(articles, list, "Scraped data should be a list.")
#         self.assertGreater(len(articles), 0, "Scraped data should contain at least one article.")
#         self.assertIn("title", articles[0], "Each article should have a title.")
#         self.assertIn("link", articles[0], "Each article should have a link.")
#         for article in articles:
#             print(f"Title: {article['title']}, Link: {article['link']}")


# class TestUNNewsAfricaScraper(unittest.TestCase):
#     def test_scrape_un_news_africa(self):
#         # Scrape data
#         articles = scrape_un_news_africa()

#         # Ensure the result is a list
#         self.assertIsInstance(articles, list, "Scraped data should be a list.")
#         # Ensure there is at least one filtered article
#         self.assertGreater(len(articles), 0, "Scraped data should contain at least one relevant article.")
#         # Check that each article contains a title and a link
#         for article in articles:
#             self.assertIn("title", article, "Each article should have a title.")
#             self.assertIn("link", article, "Each article should have a link.")

#         # Print the filtered articles
#         print("\nFiltered Articles:")
#         for article in articles:
#             print(f"Title: {article['title']}, Link: {article['link']}")



class TestDailyNationScraper(unittest.TestCase):
    def test_scrape_daily_nation(self):
        query_url = "https://nation.africa/service/search/kenya/290754?query=human%20trafficking%20in%20east%20africa%20&sortByDate=true"
        data = scrape_daily_nation_specific(query_url)
        self.assertIsNotNone(data, "Scraped data should not be None.")
        self.assertIsInstance(data, list, "Scraped data should be a list.")
        self.assertGreater(len(data), 0, "Scraped data should contain at least one article.")
        self.assertIn("title", data[0], "Each article should have a title.")
        self.assertIn("link", data[0], "Each article should have a link.")