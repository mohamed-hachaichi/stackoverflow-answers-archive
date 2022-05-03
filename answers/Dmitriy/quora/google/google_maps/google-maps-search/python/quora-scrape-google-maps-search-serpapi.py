from serpapi import GoogleSearch
import json

params = {
    "api_key": "serpapi api key",        # your serpapi api key
    "engine": "google_maps",             # search engine
    "type": "search",                    # type of google maps search results
    "q": "barbear shop new york",        # search query
    "hl": "en"                           # language
}

search = GoogleSearch(params)            # where data extracts 
results = search.get_dict()              # JSON -> Python dict

for place in results["local_results"]:
    print(json.dumps(place, indent=2, ensure_ascii=False))
    