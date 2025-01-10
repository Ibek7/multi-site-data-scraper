import requests
from bs4 import BeautifulSoup

# Not working 

def scrape_daily_nation_specific(query_url):
    """
    Scrape the Daily Nation Kenya search results for a specific query.
    Args:
        query_url (str): The URL containing the search query.
    Returns:
        list: A list of dictionaries containing title, link, and summary of the articles.
    """
    print(f"Scraping from URL: {query_url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(query_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        article_selector = "h3.title-small a"
        summary_selector = "p.teaser-image-right_paragraph"

        articles = soup.select("li.search-result")
        scraped_articles = []

        for article in articles:
            title_element = article.select_one(article_selector)
            summary_element = article.select_one(summary_selector)
            
            if title_element:
                title = title_element.text.strip()
                link = title_element["href"]
                summary = summary_element.text.strip() if summary_element else "No summary available"
                
                scraped_articles.append({
                    "title": title,
                    "link": link,
                    "summary": summary
                })

        print(f"Scraped {len(scraped_articles)} articles from {query_url}")
        return scraped_articles

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {query_url}: {e}")
        return []