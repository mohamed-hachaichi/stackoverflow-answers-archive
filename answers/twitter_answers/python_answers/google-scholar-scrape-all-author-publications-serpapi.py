import pandas as pd
import os
from serpapi import GoogleScholarSearch
from urllib.parse import urlsplit, parse_qsl


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
            title = article["title"]
            link = article["link"]
            authors = article["authors"]
            publication = article.get("publication")
            citation_id = article["citation_id"]

            print(title)

            all_articles.append({
                "title": title,
                "link": link,
                "authors": authors,
                "publication": publication,
                "citation_id": citation_id
                })

        if "next" in results.get("serpapi_pagination", []):
            # split URL in parts as a dict() and update "search" variable to a new page
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            articles_is_present = False

    pd.DataFrame(data=all_articles).to_csv(f"serpapi_google_scholar_{params['author_id']}_articles.csv", encoding="utf-8", index=False)


serpapi_scrape_all_author_articles(author_id="VjJm3zYAAAAJ")
