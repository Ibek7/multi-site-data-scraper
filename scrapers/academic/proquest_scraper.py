import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#NOT YET TESTED 

def scrape_proquest_with_selenium(query_url):
    """
    Scrape articles from ProQuest search results using Selenium.
    Args:
        query_url (str): The URL containing the search query.
    Returns:
        list: A list of dictionaries containing title and link of the articles.
    """
    print(f"Scraping from URL: {query_url}")
    
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("/path/to/chromedriver")  # Update with the actual chromedriver path

    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 20)
    
    try:
        driver.get(query_url)

        # Wait for the articles to load
        articles = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "truncatedResultsTitle")))

        scraped_articles = []
        for article in articles:
            try:
                title = article.text.strip()
                link_element = article.find_element(By.XPATH, "./ancestor::a")
                link = link_element.get_attribute("href")
                scraped_articles.append({"title": title, "link": link})
            except Exception as e:
                print(f"Error extracting article: {e}")

        print(f"Scraped {len(scraped_articles)} articles.")
        return scraped_articles

    except Exception as e:
        print(f"Error scraping {query_url}: {e}")
        return []

    finally:
        driver.quit()