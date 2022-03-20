# https://stackoverflow.com/questions/41811658/python-shows-same-results-for-every-page-beautiful-soup
# https://replit.com/@DimitryZub1/Python-shows-same-results-for-every-page-Beautiful-Soup#main.py

from bs4 import BeautifulSoup
import requests, lxml, os

params = {
    "q": "samsung",
    "hl": "en",
    "start": "0"
}

proxies = {
    "http": os.getenv("HTTP_PROXY")
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    "server": "scholar",
    "referer": f"https://scholar.google.com/scholar?hl={params['hl']}&q={params['q']}",
}

html = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, proxies=proxies, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

next_page_token = soup.select_one(".gs_ico_nav_page")
current_page = soup.select_one(".gs_ico_nav_page")

print(next_page_token, current_page, sep="\n")

# while next_page_token:
#     for result in soup.select(".gs_rt"):
#         title = result.text


