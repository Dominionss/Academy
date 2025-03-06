import requests


def download_robots_txt(url, save_path):
    """Downloads the robots.txt file from a given URL and saves it to a specified path."""
    robots_url = f"{url}/robots.txt"
    try:
        response = requests.get(robots_url)
        response.raise_for_status()
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Downloaded robots.txt from {url} and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download robots.txt from {url}: {e}")

websites = [
    ("https://www.wikipedia.org", "wikipedia_robots.txt"),
    ("https://www.twitter.com", "twitter_robots.txt"),
    ("https://www.google.com", "google_robots.txt"),
    ("https://www.facebook.com", "facebook_robots.txt"),
]


for url, save_path in websites:
    download_robots_txt(url, save_path)
