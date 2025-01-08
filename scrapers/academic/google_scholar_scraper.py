import yaml
from scholarly import scholarly
from utils.logger import get_logger

logger = get_logger(__name__)

def load_google_scholar_config(config_file):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config["google_scholar"]

def scrape_google_scholar(config_path="configs/academic.yaml"):
    """
    Scrape articles from Google Scholar based on the config file.
    """
    try:
        config = load_google_scholar_config(config_path)
        query = config["search_query"]
        num_results = config["num_results"]

        logger.info(f"Starting Google Scholar scraper for query: {query}")
        search_query = scholarly.search_pubs(query)
        articles = []

        for _ in range(num_results):
            try:
                result = next(search_query)
                article = {
                    "title": result.get("bib", {}).get("title", ""),
                    "authors": result.get("bib", {}).get("author", ""),
                    "link": result.get("pub_url", ""),
                }
                articles.append(article)
                logger.info(f"Scraped article - Title: {article['title']}, Authors: {article['authors']}, Link: {article['link']}")
            except StopIteration:
                logger.info("No more results available.")
                break

        logger.info(f"Scraped {len(articles)} articles successfully.")
        return articles

    except Exception as e:
        logger.error(f"Error scraping Google Scholar: {e}")
        return None