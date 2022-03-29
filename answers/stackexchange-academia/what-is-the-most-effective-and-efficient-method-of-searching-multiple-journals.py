import os, json
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl

params = {
    # os.getenv(): https://docs.python.org/3/library/os.html#os.getenv
    "api_key": os.getenv("API_KEY"),  # Your Serpapi API key
    "engine": "google_scholar",       # search engine
    #  search query
    "q": '"invasive species management" OR "biological invasion" source:"ecology letters" OR source:"ecological economics"',
    "hl": "en",                       # language
    # "as_ylo": "2017",               # from 2017
    # "as_yhi": "2021",               # to 2021
    "start": "0"                      # first page
    }

search = GoogleSearch(params)         # where data extraction happens

organic_results_data = []

papers_is_present = True
while papers_is_present:
    results = search.get_dict()      # JSON -> Python dictionary

    print(f"Currently extracting page №{results.get('serpapi_pagination', {}).get('current')}..")

    for result in results["organic_results"]:
        position = result["position"]
        title = result["title"]
        publication_info_summary = result["publication_info"]["summary"]
        result_id = result["result_id"]
        link = result.get("link")
        result_type = result.get("type")
        snippet = result.get("snippet")

        organic_results_data.append({
            "page_number": results.get("serpapi_pagination", {}).get("current"),
            "position": position + 1,
            "result_type": result_type,
            "title": title,
            "link": link,
            "result_id": result_id,
            "publication_info_summary": publication_info_summary,
            "snippet": snippet,
            })

        if "next" in results.get("serpapi_pagination", {}):
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            papers_is_present = False

print(json.dumps(organic_results_data, indent=2, ensure_ascii=False))