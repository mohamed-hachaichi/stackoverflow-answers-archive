# https://stackoverflow.com/questions/39680911/python-beautifulsoup-searching-google/71659631#71659631
# https://replit.com/@DimitryZub1/python-beautifulsoup-searching-google#main.py

from bs4 import BeautifulSoup
from serpapi import GoogleSearch
import requests, lxml, os

def bs4_scrape():
    with open("company_names.txt", mode="r") as in_file, \
         open("saved_company_names.txt", mode="w") as out_file:
        # read company names
        companies_list = [line.strip() for line in in_file.readlines()]

        for company_name in companies_list:
            # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
            params = {
                "q": f"{company_name} press release",
                "hl": "en",
                "gl": "us"
                }

            # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4758.87 Safari/537.36",
                }

            html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
            soup = BeautifulSoup(html.text, "lxml")

            if "press" or "press-releases" or "press-release" or "PressReleases" or "pressreleases" in soup.select_one(".yuRUbf a")["href"]:
                out_file.write(f'{soup.select_one(".yuRUbf a")["href"]}\n')


def serpapi_scrape():
    with open("company_names.txt", mode="r") as in_file, \
         open("saved_company_names_serpapi.txt", mode="w") as out_file:
        # read company names
        companies_list = [line.strip() for line in in_file.readlines()]

        for company_name in companies_list:
            params = {
                "api_key": os.getenv("API_KEY"),
                "engine": "google",
                "q": f"{company_name} press release",
                "gl": "us",
                "hl": "en"
                }

            search = GoogleSearch(params)
            results = search.get_dict()

            if "press" or "press-releases" or "press-release" or "PressReleases" or "pressreleases" in results["organic_results"][0]["link"]:
                out_file.write(f'{results["organic_results"][0]["link"]}\n')

serpapi_scrape()