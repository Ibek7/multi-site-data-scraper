import logging
import requests
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_reuters_africa(config_path="configs/news.yaml"):
    """
    Scrape news articles from Reuters Africa section.
    
    Args:
        config_path (str): Path to the configuration file (default: "configs/news.yaml").
    
    Returns:
        list: List of dictionaries containing title, link, and published_time for each article.
    """
    try:
        logger.info("Starting Reuters Africa scraper...")
        # Define the target URL and headers
        url = "https://www.reuters.com/world/africa/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
        }
        
        # Send the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logger.info(f"Successfully fetched data from {url}")
        
        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        articles = []
        
        # Find all article elements based on the selector
        for article in soup.select("a[data-testid='Heading']"):
            title = article.text.strip()
            link = article["href"]
            # Ensure full URL if the link is relative
            if not link.startswith("http"):
                link = f"https://www.reuters.com{link}"
            
            # Extract publication time if available
            time_element = article.find_next("time[data-testid='Label']")
            published_time = time_element["datetime"] if time_element else None
            
            # Append article details to the list
            articles.append({
                "title": title,
                "link": link,
                "published_time": published_time,
            })
            logger.info(f"Scraped article - Title: {title}, Link: {link}, Published Time: {published_time}")
        
        return articles

    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error while scraping Reuters Africa: {req_err}")
        return None
    except Exception as e:
        logger.error(f"Error scraping Reuters Africa: {e}")
        return None