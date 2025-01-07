from scrapers.academic.pubmed_scraper import scrape_pubmed

if __name__ == "__main__":
    print("Running PubMed Scraper...")
    scrape_pubmed(term="machine learning")
