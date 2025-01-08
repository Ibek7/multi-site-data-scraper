from bs4 import BeautifulSoup
import requests

def scrape_mail_guardian():
    url = "https://mg.co.za"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch URL: {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    # Scrape headlines in different sections
    # Search for h2 and h3 tags with links in various divs
    for section in soup.find_all(["section", "div"], class_=["headline", "row", "commercial-box", "opinion-two-meta"]):
        for article_tag in section.find_all("a", href=True):
            title_tag = article_tag.find(["h2", "h3"])
            if title_tag:
                articles.append({
                    "title": title_tag.get_text(strip=True),
                    "link": article_tag['href']
                })

    # Ensure unique links and titles
    unique_articles = {article["link"]: article for article in articles}
    return list(unique_articles.values())

if __name__ == "__main__":
    articles = scrape_mail_guardian()
    if articles:
        for article in articles:
            print(f"Title: {article['title']}, Link: {article['link']}")
    else:
        print("No articles found.")