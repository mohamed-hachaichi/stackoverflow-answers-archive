# https://stackoverflow.com/questions/56621735/xpath-getting-a-specific-set-of-elements-within-a-class/56621951#56621951

from parsel import Selector
from serpapi import GoogleScholarSearch
import requests, os

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "biology",
    "hl": "en"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

html = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, timeout=30)
selector = Selector(html.text)

for cite_by in selector.xpath('//*[@class="gs_fl"]/a[3]/@href'):
    cited_by_link = f"https://scholar.google.com/{cite_by.get()}"
    print(cited_by_link)

# ---------------------------------------------------------------------

params = {
    "api_key": os.getenv("API_KEY"), # SerpApi API key
    "engine": "google_scholar",      # scraping search engine
    "q": "biology",                  # search query
    "hl": "en"                       # langugage
}

search = GoogleScholarSearch(params)
results = search.get_dict()

for cited_by in results["organic_results"]:
    cited_by_link = cited_by["inline_links"]["cited_by"]["link"]
    print(cited_by_link)
