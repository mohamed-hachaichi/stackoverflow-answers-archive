# https://stackoverflow.com/questions/61854976/webscraping-google-search-results-using-google-api-returns-same-result-over-an
# https://replit.com/@chukhraiartur/stackoverflow-webscraping-google-search-results-using-google#main.py

from serpapi import GoogleSearch
import os

query = input("Enter the query:\n")

params = {
  # https://docs.python.org/3/library/os.html#os.getenv
  "api_key": os.getenv("API_KEY"),  # your serpapi api key
  "engine": "google",               # search engine
  "q": query                        # search query
  # other parameters
}

search = GoogleSearch(params)  # where data extraction happens on the SerpApi backend
results = search.get_dict()    # JSON -> Python dict

for result in results["organic_results"]:
    print(result["title"], result["link"], result["snippet"], sep="\n", end="\n\n")
