from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from bs4 import BeautifulSoup

# Global variable to store relevant articles
articles = []

def matches_criteria(text):
    """Check if the text matches the specified criteria."""
    global articles
    if len(articles) >= 20:
        return False  # Stop further checks if the limit is reached

    keywords = [
        "Human trafficking", "modern slavery", "labor exploitation", "sexual exploitation",
        "East Africa", "Ethiopia", "Kenya", "Uganda", "Tanzania",
        "refugees", "NGOs combating trafficking", "border control", "UN reports"
    ]
    return any(keyword.lower() in text.lower() for keyword in keywords)


def fetch_article_content(url):
    """Fetch the content of an article from its URL."""
    global articles
    if len(articles) >= 20:
        return ""  # Stop fetching content if the limit is reached

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract the main content of the article (modify the selector based on the site structure)
        content_element = soup.select_one("div.content")  # Example: Adjust selector as needed
        if content_element:
            return content_element.get_text(strip=True)
        return ""
    except Exception as e:
        print(f"Error fetching article content from {url}: {e}")
        return ""


def scrape_un_news_africa():
    """Scrape UN News Africa and filter articles based on title and content."""
    global articles  # Use the global variable to store articles
    chrome_service = ChromeService(executable_path="/Users/bekamguta/Documents/chromedriver-mac-arm64/chromedriver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        base_url = "https://news.un.org/en/news/region/africa"
        driver.get(base_url)
        visited_pages = set()

        while True:
            if len(articles) >= 20:
                print("Collected 20 relevant articles. Stopping pagination.")
                break

            current_url = driver.current_url
            print(f"Scraping page: {current_url}")

            # Check if the page is already visited
            if current_url in visited_pages:
                print(f"Already visited {current_url}, stopping to avoid infinite loop.")
                break
            visited_pages.add(current_url)

            # Scrape articles on the current page
            articles_elements = driver.find_elements(By.CSS_SELECTOR, "span.field.field--name-title")
            print(f"Found {len(articles_elements)} articles on this page.")
            for element in articles_elements:
                if len(articles) >= 20:
                    print("Collected 20 relevant articles. Stopping pagination.")
                    break

                title = element.text.strip()
                parent_element = element.find_element(By.XPATH, "..")
                link = parent_element.get_attribute("href")

                if title and link:
                    # Fetch the article content
                    content = fetch_article_content(link)

                    # Check if title or content matches criteria
                    if matches_criteria(title) or matches_criteria(content):
                        articles.append({"title": title, "link": link, "content": content})
                        print(f"Relevant article found: {title}")

            # Stop the pagination if 20 articles are collected
            if len(articles) >= 20:
                break

            # Locate and click the "Next" button or stop if not available
            try:
                next_page_element = driver.find_element(By.CSS_SELECTOR, "ul.pagination li a[rel='next']")
                driver.execute_script("arguments[0].scrollIntoView();", next_page_element)
                ActionChains(driver).move_to_element(next_page_element).click().perform()
                time.sleep(2)  # Wait for the next page to load
            except Exception as e:
                print(f"No more pages to scrape or an error occurred: {e}")
                break

    finally:
        driver.quit()

    print("Scraped Articles:")
    for article in articles:
        print(f"Title: {article['title']}, Link: {article['link']}")
    return articles


# Call the function to test
scraped_articles = scrape_un_news_africa()
print(f"Total relevant articles scraped: {len(scraped_articles)}")