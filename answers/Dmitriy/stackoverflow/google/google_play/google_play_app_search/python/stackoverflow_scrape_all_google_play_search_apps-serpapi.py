from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import json

params = {
    "api_key": "your serpapi api key",
    "engine": "google_play",      # search engine
    "hl": "en",                   # language
    "store": "apps",              # store filter: apps, books, movies
    "gl": "us",                   # country of the search
    "q": "quotes"                 # search query
}

search = GoogleSearch(params)   # where data extraction happens

apps_data = []

index = 0
apps_is_present = True
while apps_is_present:
    results = search.get_dict()  # JSON -> Python dict

    index += 1

    for result in results["organic_results"]:
        for app in result["items"]:

            apps_data.append({
                "page": index,
                "title": app.get("title"),
                "link": app.get("link"),
                "product_id": app.get("product_id"),
                "description": app.get("description"),
                "rating": app.get("rating")
            })
        
    # if next page is there, grab it and pass to GoogleSearch()
    # otherwise, stop.
    if "next" in results.get("serpapi_pagination", []):
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
    else:
        apps_is_present = False


print(json.dumps(apps_data, indent=2, ensure_ascii=False))
