# https://stackoverflow.com/questions/34479656/scrape-google-with-python-what-is-the-correct-url-for-requests-get
# https://replit.com/@DimitryZub1/Scrape-Google-with-Python-What-is-the-correct-URL-for-requ#main.py

from bs4 import BeautifulSoup
import requests, lxml, json

params = {
    "q": "caracas arepa bar google",
    "gl": "us"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

if soup.select_one(".liYKde"):
    place_name = soup.select_one(".PZPZlf.q8U8x span").text
    place_type = soup.select_one(".YhemCb+ .YhemCb").text
    place_reviews = soup.select_one(".hqzQac span").text
    place_rating = soup.select_one(".Aq14fc").text

    print(place_name, place_type, place_reviews, place_rating, sep="\n")
