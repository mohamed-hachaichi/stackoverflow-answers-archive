# https://stackoverflow.com/questions/55857189/how-to-retrieve-yahoo-search-results
# https://replit.com/@chukhraiartur/how-to-retrieve-yahoo-search-results#main.py

from serpapi import YahooSearch
import os

# You must enter your API_KEY
params = {
  "api_key": os.getenv("API_KEY"),
  "engine": "yahoo",
  "p": "deep"
}

search = YahooSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(result["title"], result["link"], sep="\n")
