from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import json, os

def serpapi_scrape():
    # https://docs.python.org/3/library/os.html#os.getenv
    params = {
      "api_key": os.getenv("API_KEY"),     # your serpapi api key
      "engine": "google_play_product",     # search engine
      "store": "apps",                     # 
      "gl": "es",                          # country to search from: Spain
      "product_id": "com.nintendo.zara",   # app ID
      "all_reviews": "true"                # show all reviews
    }
    
    search = GoogleSearch(params)          # where data extraction happens
    results = search.get_dict()            # JSON -> Python dict
    
    for review in results["reviews"]:
        print(json.dumps(review, indent=2))


def serpapi_scrape_pagination():
    # https://docs.python.org/3/library/os.html#os.getenv
    params = {
      "api_key": os.getenv("API_KEY"),     # your serpapi api key
      "engine": "google_play_product",     # search engine
      "store": "apps",                     
      "gl": "es",                          # country to search from: Spain
      "product_id": "com.nintendo.zara",   # app ID
      "all_reviews": "true"                # show all reviews
    }
    
    search = GoogleSearch(params)          # where data extraction happens

    # page number
    index = 0
    
    reviews_is_present = True
    while reviews_is_present:
        results = search.get_dict()        # JSON -> Python dict

        # update page number
        index += 1
        for review in results.get("reviews", []):
            
            print(f"\npage #: {index}\n")
            print(json.dumps(review, indent=2))
            
            if "next" in results.get("serpapi_pagination", []):
                search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))
            else:
                reviews_is_present = False