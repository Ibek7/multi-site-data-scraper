import requests

def fetch_page(url, headers=None):
    """
    Fetch the content of a URL using requests.

    :param url: The URL to fetch
    :param headers: Optional HTTP headers
    :return: The content of the page, or None if the request fails
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
