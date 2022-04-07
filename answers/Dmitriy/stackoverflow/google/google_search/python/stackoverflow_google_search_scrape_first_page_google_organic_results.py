# https://stackoverflow.com/questions/34663434/how-to-scrape-data-using-google-api
# https://replit.com/@DimitryZub1/Scrape-Google-Search-First-Page-Results#main.py

from bs4 import BeautifulSoup
import requests, json, lxml
from serpapi import GoogleSearch


def bs4_scrape():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "q": "minecraft redstone ideas",  # search query
        "gl": "us",                       # country of the search
        "hl": "en"                        # language                
    }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36",
    }

    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    results = []
    
    for index, result in enumerate(soup.select(".tF2Cxc"), start=1):
        title = result.select_one(".DKV0Md").text
        link = result.select_one(".yuRUbf a")["href"]
        displayed_link = result.select_one(".tjvcx").text
        try:
            snippet = result.select_one("#rso .lyLwlc").text
        except: snippet = None
        
        results.append({
            "position": index,
            "title": title,
            "link": link,
            "displayed_link": displayed_link,
            "snippet": snippet
        })
        
    print(json.dumps(results, indent=2, ensure_ascii=False))
    
    
bs4_scrape()


def serpapi_scrape():
    params = {
        "api_key": "serpapi_key",         # your serpapi api key
        "engine": "google",               # search engine
        "q": "minecraft redstone ideas",  # search query
        "google_domain": "google.com",    # google domain
        "gl": "us",                       # country to search from
        "hl": "en"                        # language
        # other parameters
    }

    search = GoogleSearch(params)         # where data extraction happens
    results = search.get_dict()           # JSON -> Python dictionary

    data = []

    for result in results["organic_results"]:
        data.append({
            "position": result.get("position"),
            "title": result.get("title"),
            "link": result.get("link"),
            "displayed_link": result.get("displayed_link"),
            "snippet": result.get("snippet")
        })
        
    print(json.dumps(data, indent=2, ensure_ascii=False))
    
# serpapi_scrape()