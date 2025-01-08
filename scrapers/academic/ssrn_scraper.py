from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from configs import ssrn

logger = get_logger(__name__)  # Initialize logger

def scrape_ssrn(query):
    """
    Scrape article titles and links from SSRN search results using Selenium.
    """
    base_url = ssrn["base_url"]
    search_endpoint = ssrn["search_endpoint"]
    search_url = f"{base_url}{search_endpoint}?term={query}"
    article_selector = ssrn["article_selector"]

    try:
        logger.info(f"Starting SSRN scraper for query: {query}")
        logger.info(f"Constructed search URL: {search_url}")

        # Configure Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver_service = Service("/Users/bekamguta/Documents/chromedriver-mac-arm64/chromedriver")  # Path to chromedriver

        with webdriver.Chrome(service=driver_service, options=chrome_options) as driver:
            # Load the SSRN search results page
            driver.get(search_url)

            # Log the raw HTML for debugging
            logger.info("Raw HTML response:")
            logger.info(driver.page_source)

            # Wait for the search results to load
            wait = WebDriverWait(driver, 15)  # Increase timeout to 15 seconds
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, article_selector)))

            # Extract articles
            articles = []
            elements = driver.find_elements(By.CSS_SELECTOR, article_selector)
            logger.info(f"Found {len(elements)} elements with the specified selector.")

            for element in elements:
                title = element.text
                link = element.get_attribute("href")  # Extract the href attribute directly

                if link:
                    articles.append({"title": title, "link": link})
                    logger.info(f"Scraped article - Title: {title}, Link: {link}")

            return articles if articles else None

    except Exception as e:
        logger.error(f"Error scraping SSRN: {e}", exc_info=True)
        return None