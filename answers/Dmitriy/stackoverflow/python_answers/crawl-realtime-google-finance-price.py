# https://stackoverflow.com/questions/44744350/crawl-realtime-google-finance-price
# https://replit.com/@DimitryZub1/web-scraping-google-finance-to-excel-csv#main.py

from bs4 import BeautifulSoup
import requests, lxml, json
from itertools import zip_longest
import pandas as pd


def scrape_google_finance(ticker: str):
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "hl": "en",     # language
        }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    # https://www.whatismybrowser.com/detect/what-is-my-user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        }

    html = requests.get(f"https://www.google.com/finance/quote/{ticker}", params=params, headers=headers, timeout=30)
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
    

tickers = ["DIS:NYSE", "TSLA:NASDAQ", "AAPL:NASDAQ", "AMZN:NASDAQ", "NFLX:NASDAQ"]

tickers_prices = []

for ticker in tickers:
    ticker_data = scrape_google_finance(ticker=ticker)
    print(json.dumps(ticker_data, indent=2))
#     tickers_prices.append({
#         "ticker": ticker_data["ticker_info"]["title"],
#         "price": ticker_data["ticker_info"]["current_price"]
#     })

# df = pd.DataFrame(data=tickers_prices)
# df.to_csv("google_finance_live_stock.csv", index=False)
