# how-can-i-return-all-the-titles-on-the-page-along-with-the-views-year-and-chann
# https://replit.com/@DimitryZub1/how-can-i-return-all-the-titles-on-the-page-along-with-the-v

from serpapi import GoogleSearch
import os, json

# https://docs.python.org/3/library/os.html#os.getenv
params = {
    "api_key": os.getenv("API_KEY"),  # your serpapi api key
    "engine": "youtube",              # search engine
    "search_query": "earpods pro"     # search query
    # other search parameters: https://serpapi.com/youtube-search-api
    }

search = GoogleSearch(params)
results = search.get_dict()

video_results = []

for result in results["video_results"]:
    video_results.append({
        "title": result["title"],
        "link": result["link"],
        "published_date": result["published_date"],
        "views": result["views"],
        "length": result["length"],
        "description": result["description"]
    })

print(json.dumps(video_results, indent=2, ensure_ascii=False))

