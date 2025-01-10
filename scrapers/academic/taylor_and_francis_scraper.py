import requests
from bs4 import BeautifulSoup

def scrape_taylor_and_francis(query_url):
    """
    Scrape the Taylor & Francis search results for a specific query.
    Args:
        query_url (str): The URL containing the search query.
    Returns:
        list: A list of dictionaries containing title and link of the articles.
    """
    print(f"Scraping from URL: {query_url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(query_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Define selectors
        article_selector = "a.ref.nowrap"
        title_selector = "a.ref.nowrap"

        # Find articles
        articles = soup.select(article_selector)
        scraped_articles = []

        for article in articles:
            title = article.text.strip() if article else "No title available"
            link = f"https://www.tandfonline.com{article['href']}" if article.get("href") else "No link available"

            scraped_articles.append({
                "title": title,
                "link": link
            })

        print(f"Scraped {len(scraped_articles)} articles from {query_url}")
        return scraped_articles

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {query_url}: {e}")
        return []