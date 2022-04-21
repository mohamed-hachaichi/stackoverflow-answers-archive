# https://www.quora.com/How-can-I-crawl-data-from-Google-Search
# https://replit.com/@DimitryZub1/Scrape-Google-Organic-Search-results-SerpApi#main.py

from serpapi import GoogleSearch
import json

params = {
    "api_key": "serpapi key",       # your serpapi key
    "engine": "google",             # search engine
    "q": "minecraft",               # search query
    "google_domain": "google.com", 
    "gl": "us",                     # country of the search
    "hl": "en"                      # language of the search
}

search = GoogleSearch(params)     # where data extraction happens
results = search.get_dict()       # JSON -> Python dict

# just an example to show how to access the data
for result in results["organic_results"]:
    print(
        f"{result['position']}\n"
        f"{result['title']}\n"
        f"{result['link']}\n"
        f"{result['displayed_link']}\n"
        f"{result['snippet']}\n"
        )