# https://stackoverflow.com/questions/71727849/is-there-a-reasonable-way-to-webscrape-all-app-store-apps-on-a-google-play-searc/
# https://replit.com/@DimitryZub1/Scrape-All-Apps-from-Google-App-Store-Search


from bs4 import BeautifulSoup
import requests, json, lxml, re
from serpapi import GoogleSearch


def bs4_scrape():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "q": "weather",  # search query
        "c": "apps"      # display list of apps
    }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36",
    }

    html = requests.get("https://play.google.com/store/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")
    
    apps_data = []
    
    for app in soup.select(".mpg5gc"):
        title = app.select_one(".nnK0zc").text
        company = app.select_one(".b8cIId.KoLSrc").text
        description = app.select_one(".b8cIId.f5NCO a").text
        app_link = f'https://play.google.com{app.select_one(".b8cIId.Q9MA7b a")["href"]}'
        developer_link = f'https://play.google.com{app.select_one(".b8cIId.KoLSrc a")["href"]}'
        app_id = app.select_one(".b8cIId a")["href"].split("id=")[1]
        developer_id = app.select_one(".b8cIId.KoLSrc a")["href"].split("id=")[1]
        
        try:
            # https://regex101.com/r/SZLPRp/1
            rating = re.search(r"\d{1}\.\d{1}", app.select_one(".pf5lIe div[role=img]")["aria-label"]).group(0)
        except:
            rating = None
        
        thumbnail = app.select_one(".yNWQ8e img")["data-src"]
        
        apps_data.append({
            "title": title,
            "company": company,
            "description": description,
            "rating": float(rating) if rating else rating,  # float if rating is not None else rating or None
            "app_link": app_link,
            "developer_link": developer_link,
            "app_id": app_id,
            "developer_id": developer_id,
            "thumbnail": thumbnail
        })        

    print(json.dumps(apps_data, indent=2, ensure_ascii=False))

bs4_scrape()


# ---------------

def serpapi_scrape():
    params = {
        "api_key": "API KEY",      # your serpapi api key
        "engine": "google_play",   # search engine
        "hl": "en",                # language
        "store": "apps",           # apps search
        "gl": "us",                # contry to search from. Different country displays different.
        "q": "weather"             # search qeury
    }

    search = GoogleSearch(params)  # where data extracts
    results = search.get_dict()    # JSON -> Python dictionary

    apps_data = []

    for apps in results["organic_results"]:
        for app in apps["items"]:
            apps_data.append({
                "title": app.get("title"),
                "link": app.get("link"),
                "description": app.get("description"),
                "product_id": app.get("product_id"),
                "rating": app.get("rating"),
                "thumbnail": app.get("thumbnail"),
                })

    print(json.dumps(apps_data, indent=2, ensure_ascii=False))
