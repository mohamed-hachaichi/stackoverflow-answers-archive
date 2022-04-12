# https://stackoverflow.com/questions/62938110/does-google-scholar-have-an-api-available-that-we-can-use-in-our-research-applic

import json

from scholarly import scholarly
from serpapi import GoogleScholarSearch


def serpapi_solution():

    params = {
        "api_key": "Your SerpApi Key",
        "engine": "google_scholar_profiles",
        "hl": "en",
        "mauthors": "biology"
    }

    search = GoogleScholarSearch(params)
    results = search.get_dict()

    for result in results["profiles"]:
        print(json.dumps(result, indent=2))


def scholary_solution():
    authors = scholarly.search_keyword("biology")

    for author in authors:
        print(json.dumps(author, indent=2))
