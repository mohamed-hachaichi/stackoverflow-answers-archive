from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests, lxml, os, json

def bs4_scrape():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "q": "distance between zip 75000 paris and zip 75016 paris",
        "hl": "en",
        }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4758.87 Safari/537.36",
        }

    html = requests.get("https://www.google.com/search?", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")

    for result in soup.select(".uE1RRc"):
        print(result.text)


def serpapi_scrape():
    params = {
        # https://docs.python.org/3/library/os.html#os.getenv
        "api_key": os.getenv("API_KEY"), # Your SerpAPi API key
        "engine": "google",              # search engine
        "q": "what distance between zip 75000 paris and zip 75016 paris",  # query
        "hl": "en"                       # language
        # other search parameters
        }

    search = GoogleSearch(params)      # where data extraction happens
    results = search.get_dict()        # JSON -> Python dictionary

    routes = results["answer_box"]["routes"]
    print(json.dumps(routes, indent=2, ensure_ascii=False))