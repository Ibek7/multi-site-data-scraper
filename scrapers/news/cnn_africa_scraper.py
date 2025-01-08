import os
import requests
from bs4 import BeautifulSoup
import yaml

def scrape_cnn_africa():
    # Load YAML configuration
    config_path = os.path.join(os.path.dirname(__file__), "../../configs/news.yaml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    # Extract CNN Africa configuration
    cnn_config = config.get("cnn_africa")
    if not cnn_config:
        raise ValueError("CNN Africa configuration not found in news.yaml")

    url = cnn_config["base_url"] + cnn_config["endpoint"]
    article_selector = cnn_config["article_selector"]
    link_parent_selector = cnn_config["link_parent_selector"]
    link_prefix = cnn_config["link_prefix"]

    # Fetch and parse the website
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for article_element in soup.select(article_selector):
        title = article_element.get_text(strip=True)
        link_element = article_element.find_parent(link_parent_selector)
        if title and link_element:
            link = link_prefix + link_element["href"]
            articles.append({"title": title, "link": link})

    return articles