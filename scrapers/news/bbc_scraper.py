import requests
from bs4 import BeautifulSoup
from utils.logger import get_logger

logger = get_logger(__name__)  # Initialize the logger for this module

def scrape_bbc_africa():
    """
    Scrape article titles and links from BBC Africa News.
    """
    base_url = "https://www.bbc.com/news/world/africa"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    articles = []

    try:
        logger.info("Starting BBC Africa scraper...")
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Locate articles using the updated selector
        elements = soup.select("h2[data-testid='card-headline']")
        logger.info(f"Found {len(elements)} elements with h2[data-testid='card-headline']")

        for element in elements:
            title = element.get_text(strip=True)
            link_tag = element.find_parent("a")
            if link_tag and "href" in link_tag.attrs:
                link = link_tag["href"]
                if not link.startswith("http"):
                    link = f"https://www.bbc.com{link}"  # Convert relative links to absolute
                articles.append({"title": title, "link": link})
                logger.info(f"Scraped article - Title: {title}, Link: {link}")

        logger.info(f"Scraped {len(articles)} articles successfully.")
        return articles if articles else None

    except Exception as e:
        logger.error(f"Error scraping BBC Africa: {e}")
        return None