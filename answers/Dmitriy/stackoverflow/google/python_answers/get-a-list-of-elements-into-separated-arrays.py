# https://stackoverflow.com/questions/56340797/get-a-list-of-elements-into-separated-arrays
# https://replit.com/@DimitryZub1/get-a-list-of-elements-into-separated-arrays#serpapi_solution.py

from parsel import Selector
import requests, json, os, re

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "biology",  # search query
    "hl": "en"      # language
    }

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    }

html = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, timeout=30)
selector = Selector(html.text)

data = []

for result in selector.css(".gs_ri"):
    title = result.css(".gs_rt a").xpath("normalize-space()").get()

    # https://regex101.com/r/7bmx8h/1
    authors = re.search(r"^(.*?)-", result.css(".gs_a").xpath("normalize-space()").get()).group(1).strip()
    snippet = result.css(".gs_rs").xpath("normalize-space()").get()

    # https://regex101.com/r/47erNR/1
    year = re.search(r"\d+", result.css(".gs_a").xpath("normalize-space()").get()).group(0)

    # https://regex101.com/r/13468d/1
    publisher = re.search(r"\d+\s?-\s?(.*)", result.css(".gs_a").xpath("normalize-space()").get()).group(1)
    cited_by = int(re.search(r"\d+", result.css(".gs_or_btn.gs_nph+ a::text").get()).group(0))

    data.append({
        "title": title,
        "snippet": snippet,
        "authors": authors,
        "year": year,
        "publisher": publisher,
        "cited_by": cited_by
        })

print(json.dumps(data, indent=2, ensure_ascii=False))

# -----------------------------------------------------

# from serpapi import GoogleSearch
#
# def serpapi_scrape():
#     params = {
#         "api_key": os.getenv("API_KEY"),
#         "engine": "google_scholar",
#         "q": "biology",
#         "hl": "en"
#         }
#
#     search = GoogleSearch(params)
#     results = search.get_dict()
#
#     for result in results["organic_results"]:
#         print(json.dumps(result, indent=2))
