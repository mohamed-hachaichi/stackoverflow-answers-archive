# https://stackoverflow.com/questions/41348670/get-year-of-first-publication-google-scholar

from collections import namedtuple

import requests
from parsel import Selector
from serpapi import GoogleScholarSearch

def parsel_solution():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        "user": "VGoSakQAAAAJ",
        "hl": "en",
        "view_op": "citations_histogram"
    }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    }

    html = requests.get("https://scholar.google.com/citations", params=params, headers=headers, timeout=30)
    selector = Selector(html.text)

    Publications = namedtuple("Years", "first_publication")
    publications = Publications(sorted([publication.get() for publication in selector.css(".gsc_g_t::text")])[0])

    print(selector.css(".gsc_g_t::text").get())
    print(sorted([publication.get() for publication in selector.css(".gsc_g_t::text")])[0])
    print(publications.first_publication)


def serpapi_soultion():
    params = {
        "api_key": "SerpApi API KEY",
        "engine": "google_scholar_author",
        "hl": "en",
        "author_id": "VGoSakQAAAAJ"
    }

    search = GoogleScholarSearch(params)
    results = search.get_dict()

    first_publication = [year.get("year") for year in results.get("cited_by", {}).get("graph", [])][0]
    print(first_publication)
