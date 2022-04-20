# https://stackoverflow.com/questions/61854976/webscraping-google-search-results-using-google-api-returns-same-result-over-an
# https://replit.com/@chukhraiartur/stackoverflow-webscraping-google-search-results-using-google#main.py

import sys
import urllib.request
import urllib.parse
import re
from urllib.request import urlopen as ureqs
from bs4 import BeautifulSoup as soup
from googleapiclient.discovery import build

# Google Personal Search Engine information
my_api_key = "<key>"
my_cse_id = "<id>"

# Google Search
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


# Setting up so that user can input query
query = input("enter the query\n")

# Getting into printing the results
results = google_search(query, my_api_key, my_cse_id)

print("\n*********Google Search Results*********\n")

for i in range(len(results)):
    print(f"Title == {results['items'][i]['title']}")
    print(f"Link == {results['items'][i]['link']}")
    snippet = results['items'][i]['snippet'].replace('\n', "")
    html_snippet = results['items'][i]['htmlSnippet'].replace('\n', "")
    html_snippet = html_snippet.replace("<b>", "")
    html_snippet = html_snippet.replace("</b>", "")
    html_snippet = html_snippet.replace("<br>", "")
    html_snippet = html_snippet.replace("&nbsp;…", ".")
    print(f"Description == {snippet}{html_snippet}", end="\n\n")