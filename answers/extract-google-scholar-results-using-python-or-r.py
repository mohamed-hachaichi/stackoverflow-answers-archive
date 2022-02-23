# https://stackoverflow.com/questions/13200709/extract-google-scholar-results-using-python-or-r

import json

from serpapi import GoogleScholarSearch

params = {
    "api_key": "SerpApi API KEY",
    "engine": "google_scholar",
    "q": "biology",
    "hl": "en"
}

search = GoogleScholarSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(json.dumps(result, indent=2))
