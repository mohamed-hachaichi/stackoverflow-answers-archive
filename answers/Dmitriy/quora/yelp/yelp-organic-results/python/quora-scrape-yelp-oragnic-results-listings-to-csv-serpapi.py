# https://www.quora.com/Whats-the-best-way-to-scrape-Yelp-listings-to-CSV
# https://replit.com/@DimitryZub1/Yelp-scrape-organic-result-listings-to-csv-serpapi#main.py


"""
offican API:
- https://www.yelp.com/developers/documentation/v3
- https://www.yelp.com/developers/documentation/v3/rate_limiting
"""


from serpapi import GoogleSearch
import pandas as pd
import os, json


params = {
    # https://docs.python.org/3/library/os.html#os.getenv
    "api_key": os.getenv("API_KEY"),           # your serpapi api key
    "engine": "yelp",                          # search engine
    "find_loc": "Austin, TX, United States",   # location 
    "find_desc": "burger"                      # search query
}

search = GoogleSearch(params)                  # where data extracts on SerpApi backend
results = search.get_dict()                    # JSON -> Python dict (actual data is here)

# print(results.keys())                          # dict_keys(['search_metadata', 'search_parameters', 'filters', 'inline_ads', 'ads_results', 'organic_results', 'serpapi_pagination'])
# print(results["organic_results"][0].keys())    # dict_keys(['position', 'title', 'link', 'categories', 'price', 'rating', 'reviews', 'phone', 'snippet', 'service_options', 'thumbnail'])

yelp_listings = []

for result in results["organic_results"]:
    yelp_listings.append({
        "title": result.get("title"),
        "link": result.get("link"),
        "price": result.get("price"),
        "rating": result.get("rating"),
        "reviews": result.get("reviews"),
        "phone": result.get("phone"),
        "snippet": result.get("snippet"),
        "thumbnail": result.get("thumbnail")
    })
    
    # print(json.dumps(result, indent=2, ensure_ascii=False))

df = pd.DataFrame(data=yelp_listings)
df.to_csv(f"serpapi_yelp_{params['find_desc']}_listings.csv", encoding="utf-8", index=False)  # serpapi_yelp_burger_listings.csv
