# https://stackoverflow.com/questions/55857189/how-to-retrieve-yahoo-search-results
# https://replit.com/@chukhraiartur/how-to-retrieve-yahoo-search-results#main.py

from parsel import Selector
import requests

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "p": "deep"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

html = requests.get("https://search.yahoo.com/search", params=params, headers=headers, timeout=30)
soup = Selector(text=html.text)

for result in soup.css(".compTitle.options-toggle"):
    url = result.css("a::attr(href)").get()
    text = result.css("h3 > a::text").get()
    print(text, url, sep="\n")
