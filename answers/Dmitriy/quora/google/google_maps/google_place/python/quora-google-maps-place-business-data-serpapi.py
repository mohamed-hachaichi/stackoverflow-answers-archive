from serpapi import GoogleSearch
import json


params = {
  "api_key": "API_KEY",                  # your serpapi api key
  "engine": "google_maps",               # search engine
  "type": "search",
  "q": "New Madison Street Pizza",       # search query
  "hl": "en",                            # language
  "ll": "@40.7127675,-73.994359,15.54z"  # place GPS coordinates
}

search = GoogleSearch(params)  # where data extraction happens
results = search.get_dict()    # JSON -> Python dict

print(json.dumps(results["place_results"], indent=2, ensure_ascii=False))