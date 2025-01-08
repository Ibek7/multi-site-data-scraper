import requests
from bs4 import BeautifulSoup
from utils.logger import get_logger

logger = get_logger(__name__)  # Initialize the logger for this module

def scrape_aljazeera_africa():
    """
    Scrape article titles and links from Al Jazeera Africa News.
    """
    base_url = "https://www.aljazeera.com/where/africa/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    articles = []

    try:
        logger.info("Starting Al Jazeera Africa scraper...")
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Locate articles using the provided selectors
        elements = soup.select("a.u-clickable-card__link")
        logger.info(f"Found {len(elements)} elements with class 'u-clickable-card__link'")

        for element in elements:
            title_element = element.find("span")
            title = title_element.get_text(strip=True) if title_element else "No Title"
            link = element["href"]
            if not link.startswith("http"):
                link = f"https://www.aljazeera.com{link}"  # Convert relative links to absolute
            articles.append({"title": title, "link": link})
            logger.info(f"Scraped article - Title: {title}, Link: {link}")

        logger.info(f"Scraped {len(articles)} articles successfully.")
        return articles if articles else None

    except Exception as e:
        logger.error(f"Error scraping Al Jazeera Africa: {e}")
        return None