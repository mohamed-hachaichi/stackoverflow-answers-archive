# https://stackoverflow.com/questions/63322113/using-selenium-and-beautiful-soup-together
# https://replit.com/@DimitryZub1/using-selenium-and-beautiful-soup-together

from bs4 import BeautifulSoup
import requests, lxml, os
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl


def bs4_scrape_articles():
    params = {
        "user": "VjJm3zYAAAAJ",  # user-id
        "hl": "en",  # language
        "gl": "us",  # country to search from
        "cstart": 0,  # articles page. 0 is the first page
        "pagesize": "100"  # articles per page
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    }

    articles_is_present = True

    while articles_is_present:
        html = requests.post("https://scholar.google.com/citations", params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        for index, article in enumerate(soup.select("#gsc_a_b .gsc_a_t"), start=1):
            article_title = article.select_one(".gsc_a_at").text
            article_link = f'https://scholar.google.com{article.select_one(".gsc_a_at")["href"]}'
            article_authors = article.select_one(".gsc_a_at+ .gs_gray").text
            article_publication = article.select_one(".gs_gray+ .gs_gray").text

            print(f"article #{int(params['cstart']) + index}",
                  article_title,
                  article_link,
                  article_authors,
                  article_publication, sep="\n")

        # this selector is checking for the .class that contains: "There are no articles in this profile."
        # example link: https://scholar.google.com/citations?user=VjJm3zYAAAAJ&hl=en&cstart=500&pagesize=100
        if soup.select_one(".gsc_a_e"):
            articles_is_present = False
        else:
            params["cstart"] += 100  # paginate to the next page


def serpapi_scrape_articles():
    params = {
        "api_key": os.getenv("API_KEY"),
        "engine": "google_scholar_author",
        "hl": "en",
        "author_id": "VjJm3zYAAAAJ",
        "start": "0",
        "num": "100"
    }

    search = GoogleSearch(params)

    articles_is_present = True

    while articles_is_present:
        results = search.get_dict()

        for index, article in enumerate(results["articles"], start=1):
            title = article["title"]
            link = article["link"]
            authors = article["authors"]
            publication = article.get("publication")
            citation_id = article["citation_id"]

            print(f"article #{int(params['start']) + index}",
                  title,
                  link,
                  authors,
                  publication,
                  citation_id, sep="\n")

        if "next" in results["serpapi_pagination"]:
            # split URL in parts as a dict() and update "search" variable to a new page
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            articles_is_present = False
