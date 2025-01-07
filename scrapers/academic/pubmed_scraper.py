import requests
from utils.downloader import fetch_page

def scrape_pubmed(term):
    """Scrape PubMed articles based on a search term."""
    base_url = "https://pubmed.ncbi.nlm.nih.gov"
    search_url = f"{base_url}/?term={term}"
    
    try:
        page_content = fetch_page(search_url)
        if page_content:
            print(f"Successfully fetched data for term: {term}")
            # Add logic to parse the data using BeautifulSoup
        else:
            print("Failed to fetch data.")
    except Exception as e:
        print(f"Error occurred: {e}")