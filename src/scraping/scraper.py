import json
import requests
from bs4 import BeautifulSoup
from typing import List, Dict

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_transcript(url: str) -> str:
    """
    Scrape transcript text from a scrapfromtheloft.com page
    """
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")

    text_blocks = [
        p.get_text(strip=True) for p in paragraphs
        if len(p.get_text(strip=True)) > 20
    ]

    return " ".join(text_blocks)

def build_record(record: dict) -> dict:
    """
    Build a structured transcript record form registry
    """

    url = record["url"]
    transcript = scrape_transcript(url)

    return {
        "url": url,
        "comedian": record.get("comedian"),
        "special": record.get("special"),
        "transcript": transcript
    }

def scrape_multiple(registry):
    """
    Scrape multiple comedy transcripts safely
    """

    data = []
    for record in registry:
        try:
            item = build_record(record)
            if len(item["transcript"]) > 1000:
                data.append(item)
        except Exception as e:
            print(f"Failed as to scrape {record['url']}: {e}")

    return data

        
