from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Code not working, find out why!
def scrape_researchgate_with_selenium(query_url):
    """
    Scrape ResearchGate search results using Selenium.

    Args:
        query_url (str): The URL containing the search query.
    Returns:
        list: A list of dictionaries containing the title and link of the articles.
    """
    driver = None
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    options.headless = False  # Set to False for debugging

    # Update the path to your chromedriver
    service = Service(executable_path="/Users/bekamguta/Documents/chromedriver-mac-arm64/chromedriver")

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(query_url)

        # Wait for the page to load and scroll
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        # Save runtime page source for debugging
        with open("runtime_page_source.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        # Wait for the articles to load
        wait = WebDriverWait(driver, 60)
        articles = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.nova-legacy-e-link.nova-legacy-v-publication-item__title"))
        )

        # Extract article details
        scraped_data = []
        for article in articles:
            try:
                title = article.text.strip()
                link = article.get_attribute("href")
                print(f"Found article: {title}, Link: {link}")
                scraped_data.append({"title": title, "link": link})
            except Exception as e:
                print(f"Error extracting article data: {e}")

        print(f"Scraped {len(scraped_data)} articles")
        return scraped_data

    except Exception as e:
        print(f"Error: {e}")
        return []

    finally:
        if driver:
            driver.quit()