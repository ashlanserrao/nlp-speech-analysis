import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = "https://scrapsfromtheloft.com"
COMEDY_INDEX = f"{BASE_URL}/comedy/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

def discover_transcript_urls(): 
    """ Discover stand up comedy transcript urls from the site"""
    response = requests.get(COMEDY_INDEX, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    
    urls = set()

    for link in soup.find_all("a", href=True):
        href = link["href"]

        # heuristic
        if href.startswith("/20") or "/comedy/" in href:
            full_url = href if href.startswith("http") else BASE_URL + href
            urls.add(full_url)


    return sorted(urls)

def save_urls(urls, filename = "discovered_comedy_urls.json"):
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DATA_DIR / filename
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(urls, f, indent=2)

    print(f"Saved {len(urls)} URLs to {path}")

if __name__ == "__main__":
    urls = discover_transcript_urls()
    save_urls(urls)
    