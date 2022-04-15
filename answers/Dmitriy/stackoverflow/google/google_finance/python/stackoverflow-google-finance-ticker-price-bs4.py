# https://stackoverflow.com/questions/5636929/page-scraping-to-get-prices-from-google-finance
# https://replit.com/@DimitryZub1/web-scraping-from-google-finance-returned-data-list-always-e#main.py

from bs4 import BeautifulSoup
import requests, lxml, json
from itertools import zip_longest


def scrape_google_finance(ticker: str):
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "hl": "en"
        }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    # https://www.whatismybrowser.com/detect/what-is-my-user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
        }

    html = requests.get(f"https://www.google.com/finance/quote/{ticker}", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    ticker_data = {
        "ticker_data": {},
        "about_panel": {}
    }
    
    ticker_data["ticker_data"]["current_price"] = soup.select_one(".AHmHk .fxKbKc").text
    ticker_data["ticker_data"]["quote"] = soup.select_one(".PdOqHc").text.replace(" • ",":")
    ticker_data["ticker_data"]["title"] = soup.select_one(".zzDege").text
    
    right_panel_keys = soup.select(".gyFHrc .mfs7Fc")
    right_panel_values = soup.select(".gyFHrc .P6K39c")
    
    for key, value in zip_longest(right_panel_keys, right_panel_values):
        key_value = key.text.lower().replace(" ", "_")

        ticker_data["about_panel"][key_value] = value.text
    
    return ticker_data
    

data = scrape_google_finance(ticker="GOOGL:NASDAQ")

print(json.dumps(data, indent=2))
print(data["ticker_data"].get("current_price"))