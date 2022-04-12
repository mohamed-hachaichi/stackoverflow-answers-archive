# https://stackoverflow.com/questions/49539381/how-to-printout-answer-from-google-using-selenium-beautifulsoup-and-headless-go
# https://replit.com/@DimitryZub1/how-to-printout-answer-from-google-using-selenium-beautifuls#main.py

from bs4 import BeautifulSoup
import requests, lxml, os

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "How old is messi?",  # search query
    "hl": "en",                # language
    "gl": "us"                 # country to search from
    }

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    }

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

answer = soup.select_one(".Z0LcW").text
print(answer)

# -----------------

# from serpapi import GoogleSearch
# import os
#
# params = {
#     "api_key": os.getenv("API_KEY"),  # Your SerpApi API key
#     "engine": "google",               # search engine
#     "q": "How old is messi?",         # search query
#     "gl": "us",                       # country to search from
#     "hl": "en"                        # language
#     }
#
# search = GoogleSearch(params)         # where data extraction happens
# results = search.get_dict()           # JSON -> Python dictionary
#
# answer = results["answer_box"]["answer"]
# print(answer)
