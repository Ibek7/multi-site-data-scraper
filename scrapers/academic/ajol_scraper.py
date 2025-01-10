from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def scrape_ajol(query_url):
    """
    Scrape the African Journals Online (AJOL) website for search results.
    Args:
        query_url (str): The search query URL.
    Returns:
        list: A list of dictionaries containing title and link of the articles.
    """
    print(f"Scraping from URL: {query_url}")
    scraped_articles = []

    # Set up Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    service = Service(executable_path="/Users/bekamguta/Documents/chromedriver-mac-arm64/chromedriver")  # Update this with your actual ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the search query URL
        driver.get(query_url)
        time.sleep(5)  # Allow time for JavaScript to load

        # Selectors for article elements
        articles = driver.find_elements(By.CSS_SELECTOR, "div.gsc-webResult")
        print(f"Found {len(articles)} articles on the page.")

        for article in articles:
            try:
                title_element = article.find_element(By.CSS_SELECTOR, "a.gs-title")
                title = title_element.text.strip()
                link = title_element.get_attribute("href")
                scraped_articles.append({
                    "title": title,
                    "link": link,
                })
            except Exception as e:
                print(f"Error parsing article: {e}")
                continue

        # Print debugging info
        print(f"Scraped {len(scraped_articles)} articles from {query_url}")
        for article in scraped_articles:
            print(f"Title: {article['title']}, Link: {article['link']}")

        return scraped_articles

    except Exception as e:
        print(f"Error scraping {query_url}: {e}")
        return []

    finally:
        driver.quit()