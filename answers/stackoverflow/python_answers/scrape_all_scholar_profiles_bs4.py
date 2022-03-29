# https://stackoverflow.com/questions/41331881/prevent-503-error-when-scraping-google-scholar
# https://replit.com/@DimitryZub1/prevent-503-error-when-scraping-google-scholar#main.py

from bs4 import BeautifulSoup
import requests, lxml, re

import os, json
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl

def scrape_all_authors():
    params = {
        "view_op": "search_authors",
        "mauthors": "valve",
        "hl": "en",
        "astart": 0
    }

    authors_is_present = True
    while authors_is_present:

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
        }

        html = requests.get("https://scholar.google.com/citations", params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        for author in soup.select(".gs_ai_chpr"):
            name = author.select_one(".gs_ai_name a").text
            link = f'https://scholar.google.com{author.select_one(".gs_ai_name a")["href"]}'
            affiliations = author.select_one(".gs_ai_aff").text
            email = author.select_one(".gs_ai_eml").text
            try:
                cited_by = re.search(r"\d+", author.select_one(".gs_ai_cby").text).group() # Cited by 17143 -> 17143
            except: cited_by = None

            print(f"extracting authors at page #{params['astart']}.",
                  name,
                  link,
                  affiliations,
                  email,
                  cited_by, sep="\n")

        if soup.select_one("button.gs_btnPR")["onclick"]:
            params["after_author"] = re.search(r"after_author\\x3d(.*)\\x26", str(soup.select_one("button.gs_btnPR")["onclick"])).group(1)  # -> XB0HAMS9__8J
            params["astart"] += 10
        else:
            authors_is_present = False


scrape_all_authors()

def serpapi_scrape_all_authors():
    params = {
        "api_key": os.getenv("API_KEY"),      # SerpApi API key
        "engine": "google_scholar_profiles",  # profile results search engine
        "mauthors": "valve",                  # search query
    }
    search = GoogleSearch(params)

    profile_results_data = []

    profiles_is_present = True
    while profiles_is_present:

        profile_results = search.get_dict()

        for profile in profile_results["profiles"]:

            print(f'Currently extracting {profile["name"]} with {profile["author_id"]} ID.')

            thumbnail = profile["thumbnail"]
            name = profile["name"]
            link = profile["link"]
            author_id = profile["author_id"]
            affiliations = profile["affiliations"]
            email = profile.get("email")
            cited_by = profile.get("cited_by")
            interests = profile.get("interests")

            profile_results_data.append({
                "thumbnail": thumbnail,
                "name": name,
                "link": link,
                "author_id": author_id,
                "email": email,
                "affiliations": affiliations,
                "cited_by": cited_by,
                "interests": interests
            })

            if "next" in profile_results["pagination"]:
                # split URL in parts as a dict() and update search "params" variable to a new page
                search.params_dict.update(dict(parse_qsl(urlsplit(profile_results["pagination"]["next"]).query)))
            else:
                profiles_is_present = False

    return profile_results_data

# print(json.dumps(serpapi_scrape_all_authors(), indent=2))
