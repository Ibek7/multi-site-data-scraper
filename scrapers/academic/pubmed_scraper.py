from utils.downloader import fetch_page

def scrape_pubmed(term):
    base_url = "https://pubmed.ncbi.nlm.nih.gov"
    search_url = f"{base_url}/?term={term}"
    page_content = fetch_page(search_url)
    if page_content:
        print("Page content fetched successfully!")
        # Further processing logic here
