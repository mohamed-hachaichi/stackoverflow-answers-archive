import os

from bs4 import BeautifulSoup
import requests, lxml
from serpapi import GoogleSearch


def bs4_scrape_pdf():
    params = {
        "q": "entity resolution",
        "hl": "en"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    }

    html = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")

    for pdf_link in soup.select(".gs_or_ggsm a"):
      pdf_file_link = pdf_link["href"]
      print(pdf_file_link)


def serpapi_scrape_pdf():

    params = {
        "api_key": os.getenv("API_KEY"),
        "engine": "google_scholar",
        "q": "entity resolution",
        "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for pdfs in results["organic_results"]:
        for link in pdfs.get("resources", []):
            pdf_link = link["link"]
            print(pdf_link)

serpapi_scrape_pdf()
