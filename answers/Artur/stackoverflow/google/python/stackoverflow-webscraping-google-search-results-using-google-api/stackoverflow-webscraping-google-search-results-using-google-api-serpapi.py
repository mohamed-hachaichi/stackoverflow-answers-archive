# https://stackoverflow.com/questions/61854976/webscraping-google-search-results-using-google-api-returns-same-result-over-an
# https://replit.com/@chukhraiartur/stackoverflow-webscraping-google-search-results-using-google#main.py

from serpapi import GoogleSearch
import os

query = input("Enter the query:\n")

# You must enter your API_KEY
params = {
  "api_key": os.getenv("API_KEY"),
  "engine": "google",
  "q": query
}

search = GoogleSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(result["title"], result["link"], result["snippet"], sep="\n", end="\n\n")
