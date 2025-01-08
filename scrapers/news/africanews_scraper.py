import requests
from bs4 import BeautifulSoup
import logging
import yaml

"""
# Potential Issues with the Web Scraper
1. **CSS Selector Mismatch**:
   - The CSS selector ('h2.teaser_title a') may not match the current HTML structure of the website.
   - Verify the selector using browser developer tools and update if necessary.

2. **Website Anti-Scraping Measures**:
   - The website may block requests without proper headers (e.g., User-Agent).
   - Content might be dynamically loaded via JavaScript, requiring a headless browser (e.g., Selenium, Playwright).
   - Look for CAPTCHAs, redirects, or other anti-bot mechanisms in the response.

3. **Invalid YAML Configuration**:
   - Ensure the configuration file (e.g., news.yaml) contains valid keys (e.g., 'africanews' and 'selectors.article_link').

4. **Website Structural Changes**:
   - Websites frequently update their layout, which could break the scraper.
   - Check the response HTML to ensure the DOM matches the scraper's expectations.

5. **Incomplete or Broken HTTP Response**:
   - Issues like HTTP 403 (Forbidden), 500 (Internal Server Error), or timeouts may occur.
   - Ensure the response status code is 200 and the HTML content is complete.

6. **Relative URLs Not Handled Correctly**:
   - Links in the HTML might be relative (e.g., '/2025/01/08/christmas-arrives-in-ethiopia/').
   - Convert relative URLs to absolute ones using a base URL.

7. **Empty or Missing Elements**:
   - The scraper might find no elements matching the CSS selector, resulting in no articles being returned.
   - Add debugging statements to confirm whether elements are found.

# Debugging Recommendations
1. Inspect the HTTP Response:
   - Print the status code (`response.status_code`) and HTML (`response.text`) to ensure the request is successful and the content is present.

2. Validate the CSS Selector:
   - Use browser developer tools to confirm that the selector matches the intended elements.

3. Check for JavaScript-Rendered Content:
   - If articles are missing in `response.text`, consider using Selenium or Playwright for dynamic rendering.

4. Log Errors for Clarity:
   - Add detailed logging to identify issues during the scraping process, e.g., HTTP errors, empty selectors, or unexpected website structure.

"""

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def scrape_africanews(base_url="https://www.africanews.com"):
    """
    Scrapes the AfricaNews website for news articles.

    Args:
        base_url (str): Base URL of the AfricaNews website.

    Returns:
        list: A list of dictionaries containing article titles and URLs.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Updated selector
        article_selector = "div.container div.teaser__content a.teaser__title"
        articles = []

        for link in soup.select(article_selector):
            title = link.get_text(strip=True)
            url = link["href"]
            full_url = url if url.startswith("http") else f"{base_url}{url}"
            articles.append({"title": title, "link": full_url})

        # Log if no articles are found
        if not articles:
            print("No articles found.")
        return articles
    
    except Exception as e:
        print(f"Error scraping AfricaNews: {e}")
        return None