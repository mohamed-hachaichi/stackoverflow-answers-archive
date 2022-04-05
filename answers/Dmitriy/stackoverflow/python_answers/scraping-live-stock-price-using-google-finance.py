# https://stackoverflow.com/questions/68150569/scraping-live-stock-price-using-google-finance
# https://replit.com/@DimitryZub1/web-scraping-from-google-finance-returned-data-list-always-e#main.py

from bs4 import BeautifulSoup
import requests, lxml, json
from itertools import zip_longest


def scrape_google_finance(ticker: str):
    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    # https://www.whatismybrowser.com/detect/what-is-my-user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        }

    html = requests.get(f"https://www.google.com/finance/quote/{ticker}", headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    ticker_data = {"right_panel_data": {},
                    "ticker_info": {}}
    
    ticker_data["ticker_info"]["title"] = soup.select_one(".zzDege").text
    ticker_data["ticker_info"]["current_price"] = soup.select_one(".AHmHk .fxKbKc").text
    
    right_panel_keys = soup.select(".gyFHrc .mfs7Fc")
    right_panel_values = soup.select(".gyFHrc .P6K39c")
    
    for key, value in zip_longest(right_panel_keys, right_panel_values):
        key_value = key.text.lower().replace(" ", "_")

        ticker_data["right_panel_data"][key_value] = value.text
    
    return ticker_data
    

data = scrape_google_finance(ticker="INFY:NSE")

# ensure_ascii to display Indian Rupee ₹ symbol
print(json.dumps(data, indent=2, ensure_ascii=False))
print(data["right_panel_data"].get("ceo"))