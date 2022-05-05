import pandas as pd
from bs4 import BeautifulSoup
import requests, lxml, os

from serpapi import GoogleScholarSearch
from urllib.parse import urlsplit, parse_qsl



def scrape_all_authors_articles(author_id: str):
    params = {
        "user": author_id,   # user-id
        "hl": "en",          # language
        "gl": "us",          # country to search from
        "cstart": 0,         # articles page. 0 is the first page
        "pagesize": "100"    # articles per page
        }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
        }

    all_articles = []

    articles_is_present = True
    while articles_is_present:
        html = requests.post("https://scholar.google.com/citations", params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        for index, article in enumerate(soup.select(".gsc_a_tr"), start=1):
            try:
                article_title = article.select_one(".gsc_a_at").text
            except: article_title = None

            try:
                article_link = f'https://scholar.google.com{article.select_one(".gsc_a_at")["href"]}'
            except: article_link = None

            try:
                article_authors = article.select_one(".gsc_a_at+ .gs_gray").text
            except: article_authors = None

            try:
                article_publication = article.select_one(".gs_gray+ .gs_gray").text
            except: article_publication = None
                
            try:
                article_year = article.select_one(".gsc_a_hc").text
            except: article_year = None

            all_articles.append({
                "title": article_title,
                "link": article_link,
                "authors": article_authors,
                "publication": article_publication,
                "article_year": article_year
                })

        # this selector is checking for the .class that contains: "There are no articles in this profile."
        # example link: https://scholar.google.com/citations?user=VjJm3zYAAAAJ&hl=en&cstart=500&pagesize=100
        if soup.select_one(".gsc_a_e"):
            articles_is_present = False
        else:
            params["cstart"] += 100  # paginate to the next page

    pd.DataFrame(data=all_articles).to_csv(f"google_scholar_{params['user']}_articles.csv", encoding="utf-8", index=False)

user_ids = ["rUHfmpQAAAAJ", "HRkZPK4AAAAJ", "DubfkQ8AAAAJ", "VjJm3zYAAAAJ"]

for _id in user_ids:
    scrape_all_authors_articles(author_id=_id)
    
    
# SerpApi solution

import os



def serpapi_scrape_all_author_articles(author_id: str):
    params = {
        "api_key": os.getenv("API_KEY"),    # your SerpApi API key
        "engine": "google_scholar_author",  # search engine
        "hl": "en",                         # language
        "author_id": author_id,             # author ID
        "start": "0",                       # articles page
        "num": "100"                        # articles per page
        }

    search = GoogleScholarSearch(params)    # where data extraction happens on SerpApi backend.

    all_articles = []

    articles_is_present = True
    while articles_is_present:
        results = search.get_dict()         # JSON -> Python dictionary

        for index, article in enumerate(results["articles"], start=1):
            title = article.get("title")
            link = article.get("link")
            authors = article.get("authors")
            publication = article.get("publication")
            citation_id = article.get("citation_id")
            year = article.get("year")

            print(title)

            all_articles.append({
                "title": title,
                "link": link,
                "authors": authors,
                "publication": publication,
                "citation_id": citation_id,
                "year": year
                })

        if "next" in results.get("serpapi_pagination", []):
            # split URL in parts as a dict() and update "search" variable to a new page
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            articles_is_present = False

    pd.DataFrame(data=all_articles).to_csv(f"serpapi_google_scholar_{params['author_id']}_articles.csv", encoding="utf-8", index=False)


serpapi_scrape_all_author_articles(author_id="VjJm3zYAAAAJ")
