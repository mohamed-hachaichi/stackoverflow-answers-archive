# https://qr.ae/pvsjTN
# https://replit.com/@DimitryZub1/Scrape-All-Google-Images-SerpApi#main.py

from serpapi import GoogleSearch
import os, json

params = {
    # https://docs.python.org/3/library/os.html#os.getenv
    "api_key": os.getenv("API_KEY"),   # serpapi API key
    "engine": "google",                # search engine. There are also Bing, Yahoo, Naver, Baidu, etc.
    "q": "minecraft snoop dogg skin",  # search query
    "gl": "us",                        # country to search from
    "hl": "en",                        # language
    "tbm": "isch",                     # parameter to display image results
    "num": "100",                      # number of images per page
    "ijn": 0                           # page number, 0 -> first page, 1 -> second and so on
    # other params under API examples: https://serpapi.com/images-results
}

search = GoogleSearch(params)          # where data extraction happens

image_results = []

images_is_present = True
while images_is_present:
    
    print(f"Extracted #{params['ijn']} page.")
    
    # JSON -> Python dict (actual data is here)
    results = search.get_dict()

    # checks for "Google hasn't returned any results for this query."
    if "error" not in results:
        for image in results["images_results"]:
            if image["original"] not in image_results:  
                image_results.append(image["original"])
        
        # update to the next page
        params["ijn"] += 1
        print(params["ijn"])
    else:
        images_is_present = False
        print(results["error"])


print(json.dumps(image_results, indent=2))
print(len(image_results))


