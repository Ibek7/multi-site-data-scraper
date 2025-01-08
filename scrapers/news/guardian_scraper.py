import requests
from bs4 import BeautifulSoup
from utils.logger import get_logger
import yaml

logger = get_logger(__name__)  # Initialize the logger for this module

def scrape_guardian_global_development():
    """
    Scrape article titles and links from The Guardian - Global Development.
    """
    try:
        # Load the configuration from the YAML file
        with open("configs/news.yaml", "r") as file:
            config = yaml.safe_load(file)

        # Extract URL and selector for The Guardian
        base_url = config["guardian"]["url"]
        selector = config["guardian"]["selectors"]["article_link"]

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        articles = []

        logger.info("Starting The Guardian - Global Development scraper...")
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrape using the selector from the YAML configuration
        elements = soup.select(selector)
        logger.info(f"Found {len(elements)} elements with selector '{selector}'")

        for element in elements:
            title = element.get_text(strip=True)
            link = element["href"]
            if not link.startswith("http"):
                link = f"https://www.theguardian.com{link}"  # Convert relative links to absolute
            articles.append({"title": title, "link": link})
            logger.info(f"Scraped article - Title: {title}, Link: {link}")

        logger.info(f"Scraped {len(articles)} articles successfully.")
        return articles if articles else None

    except Exception as e:
        logger.error(f"Error scraping The Guardian - Global Development: {e}")
        return None