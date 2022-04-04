# https://stackoverflow.com/questions/55857189/how-to-retrieve-yahoo-search-results
# https://replit.com/@chukhraiartur/how-to-retrieve-yahoo-search-results#main.py

from bs4 import BeautifulSoup
import requests, lxml

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "p": "deep"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

html = requests.get("https://search.yahoo.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

for result in soup.select(".compTitle.options-toggle"):
    url = result.select_one("a")["href"]
    text = list(result.select_one("a").text)

    for i in range(len(result.select_one("span").text)):
        text.pop(0)
        
    print("".join(text), url, sep="\n")
