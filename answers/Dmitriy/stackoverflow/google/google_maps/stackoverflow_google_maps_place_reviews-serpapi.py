# https://www.quora.com/unanswered/How-can-I-mine-data-from-Google-Maps
# https://replit.com/@DimitryZub1/Scrape-Google-Maps-Place-First-10-Review-SerpApi#main.py


from serpapi import GoogleSearch
import os, json


params = {
    # https://docs.python.org/3/library/os.html#os.getenv
    
    "api_key": os.getenv("API_KEY"),                    # your serpapi api key
    "engine": "google_maps_reviews",                    # search engine
    "hl": "en",                                         # language
    "data_id": "0x89c259a61c75684f:0x79d31adb123348d2"  # place ID
}

search = GoogleSearch(params)                    # where data extraction happens on the SerpApi backend
results = search.get_dict()                      # JSON -> Python dict

# print(results["reviews"][0].keys())              # to show available reviews data keys
# print(results["reviews"][0]["user"].keys())      # to show available user data keys

for review in results["reviews"]:
    # print(json.dumps(review["user"], indent=2))  # extracts users data who left a review
    print(json.dumps(review, indent=2))          # extracts actual review data
    
    # examples of accessing data: 
        
    # name = review["user"]["name"]
    # link = review["user"]["link"]
    # thumbnail = review["user"]["thumbnail"]
    # local_guide = review["user"]["local_guide"]
    # reviews = review["user"]["reviews"]
    # photos = review["user"]["photos"]
    # date_published = review["date"]
    # review_text = review["snippet"]
    # likes = review["likes"]
    # images = review["images"]
