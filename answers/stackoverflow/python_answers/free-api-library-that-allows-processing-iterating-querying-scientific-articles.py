# https://stackoverflow.com/questions/56141694/free-api-library-that-allows-processing-iterating-querying-scientific-articles

import json

from serpapi import GoogleScholarSearch

params = {
    "api_key": "836284cf3857a908d9a5bd2a4895fca5d5950dd2379f7ddf0300bd4471c37a2b",
    "engine": "google_scholar",
    "q": "biology",
    "hl": "en"
}

search = GoogleScholarSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(json.dumps(result, indent=2))
