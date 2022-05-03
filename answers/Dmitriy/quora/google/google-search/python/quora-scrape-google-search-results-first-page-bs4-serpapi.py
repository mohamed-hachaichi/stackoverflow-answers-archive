from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests, lxml, os

def bs4_scrpae():
    params = {
        "q": "lion",  # search query
        "hl": "en",   # language of the search
        "gl": "us"    # country of the search
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
    }

    html = requests.get(f"https://www.google.com/search", headers=headers, params=params)
    soup = BeautifulSoup(html.text, "lxml")

    for container in soup.select(".tF2Cxc"):
        title = container.select_one(".DKV0Md").text
        link = container.select_one(".yuRUbf a")["href"]
        print(title, link, end="\n\n")

bs4_scrpae()

# Serpapi solution

def serpapi_scrape():
    params = {
        # https://docs.python.org/3/library/os.html#os.getenv
        "api_key": os.getenv("API_KEY"),  # serpapi api key
        "engine": "google",               # search engine
        "q": "fus ro dah",                # search query
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for result in results['organic_results']:
        print(f"Title: {result.get('title')}\n"
            f"Snippet: {result.get('snippet')}\n"
            f"Link: {result.get('link')}\n")

# serpapi_scrape()