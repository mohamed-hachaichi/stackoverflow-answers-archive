# https://stackoverflow.com/questions/71069101/discord-google-image-search-bot
# https://replit.com/@DimitryZub1/discord-google-image-search-bot#main.py

from serpapi import GoogleSearch
import os, json

params = {
    "api_key": os.getenv("API_KEY"),   # serpapi API key
    "engine": "google",                # search engine. There are also Bing, Yahoo, Naver, Baidu, etc.
    "q": "fus ro dah",                 # search query
    "gl": "us",                        # country to search from
    "hl": "en",                        # language
    "tbm": "isch"                      # parameter to display image results
    # other params under API examples: https://serpapi.com/images-results
}

search = GoogleSearch(params)
results = search.get_dict()

image_results = []

for image in results["images_results"]:
    image_results.append({
        "thumbnail": image["thumbnail"],
        "original": image["original"]
        })

print(json.dumps(image_results, indent=2))


