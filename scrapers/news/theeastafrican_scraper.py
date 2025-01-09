from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import os

def scrape_theeastafrican():
    # Load configuration
    config_path = os.path.join("configs", "news.yaml")
    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    
    site_config = config.get("theeastafrican")
    if not site_config:
        raise ValueError("No configuration found for The East African.")
    
    url = site_config["url"]
    article_selector = site_config["selectors"]["article_title"]

    # Initialize Selenium WebDriver
    service = Service("/Users/bekamguta/Documents/chromedriver-mac-arm64/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36")

    driver = webdriver.Chrome(service=service, options=options)
    articles = []

    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, article_selector))
        )
        
        # Find articles
        article_elements = driver.find_elements(By.CSS_SELECTOR, article_selector)
        for element in article_elements:
            title = element.text
            link = element.find_element(By.XPATH, "./ancestor::a").get_attribute("href")
            articles.append({"title": title, "link": link})
        
        print(f"Fetched articles: {articles}")  # Debugging
    except Exception as e:
        print(f"Failed to fetch URL: {url}, Error: {e}")
    finally:
        driver.quit()

    return articles