from serpapi import GoogleSearch
import os

params = {
    # https://docs.python.org/3/library/os.html#os.getenv
    "api_key": os.getenv("API_KEY"),  # serpapi api key
    "engine": "google",               # search engine
    "q": "fus ro dah",                # search query
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results['organic_results']:
    title = result.get('title')
    link = result.get('link')
    snippet = result.get('snippet')
    
    print(title, link, snippet, end="\n\n")