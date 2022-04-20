# https://stackoverflow.com/questions/61854976/webscraping-google-search-results-using-google-api-returns-same-result-over-an
# https://replit.com/@chukhraiartur/stackoverflow-webscraping-google-search-results-using-google#main.py

from bs4 import BeautifulSoup
import requests, lxml

query = input("Enter the query:\n")

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": query
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

for result in soup.select(".tF2Cxc"):
    title = "Title == " + result.select_one("h3").text
    link = "Link == " + result.select_one("a")["href"]
    description = "Description == " + result.select_one(".VwiC3b").text

    print(title, link, description, sep="\n", end="\n\n")
