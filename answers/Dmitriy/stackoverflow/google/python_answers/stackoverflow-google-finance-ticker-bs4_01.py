# https://stackoverflow.com/questions/48948161/python-scraping-google-finance
# https://replit.com/@DimitryZub1/web-scraping-from-google-finance-returned-data-list-always-e#main.py

from bs4 import BeautifulSoup
import requests, lxml, json

# https://docs.python.org/3/library/itertools.html#itertools.zip_longest
from itertools import zip_longest 


def scrape_google_finance(ticker: str):
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "hl": "en"
        }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    # https://www.whatismybrowser.com/detect/what-is-my-user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        }

    html = requests.get(f"https://www.google.com/finance/quote/{ticker}", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    right_panel_data = {"right_panel": {}}
    
    right_panel_keys = soup.select(".gyFHrc .mfs7Fc")
    right_panel_values = soup.select(".gyFHrc .P6K39c")
    
    for key, value in zip_longest(right_panel_keys, right_panel_values):
        key_value = key.text.lower().replace(" ", "_")

        right_panel_data["right_panel"][key_value] = value.text
    
    return right_panel_data
    

data = scrape_google_finance(ticker="GOOGL:NASDAQ")

print(json.dumps(data, indent=2))

print(data["right_panel"].keys())
print(data["right_panel"].get("p/e_ratio"))