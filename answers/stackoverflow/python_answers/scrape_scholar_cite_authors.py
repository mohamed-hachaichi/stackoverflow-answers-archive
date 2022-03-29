from bs4 import BeautifulSoup
import requests, lxml, json

params = {
    "q": "automated container terminal",
    "hl": "en"
}
proxies = {
    # "http": FreeProxy(country_id=["US"], https=False, rand=True).get()
    # "http": "http://2CH8vhoXpDouoog:xMqL4guJQ8yjnlq@server.proxyland.io:9090"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    "server": "scholar",
    "referer": f"https://scholar.google.com/scholar?hl={params['hl']}&q={params['q']}",
}


def cite_ids() -> list:
    response = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, "lxml")

    # returns a list of publication ID's -> U8bh6Ca9uwQJ
    return [result["data-cid"] for result in soup.select(".gs_or")]

def scrape_cite_results() -> list:
    cited_authors = []

    for cite_id in cite_ids():
        response = requests.get(f"https://scholar.google.com/scholar?output=cite&q=info:{cite_id}:scholar.google.com", headers=headers, proxies=proxies)
        soup = BeautifulSoup(response.text, "lxml")

        for result in soup.select("tr"):
            if "APA" in result.select_one("th"):
                title = result.select_one("th").text
                authors = result.select_one("td").text

                cited_authors.append({"title": title, "cited_authors": authors})

    return cited_authors

print(json.dumps(scrape_cite_results(), indent=2))
#
# from parsel import Selector
# import requests, json
#
# params = {
#     "q": "automated container terminal",
#     "hl": "en"
# }
#
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.3538.102 Safari/537.36 Edge/18.19582",
#     'accept-language': 'en-US,en',
#     'accept': 'text/html,application/xhtml+xml,application/xml',
#     "server": "scholar",
#     "referer": f"https://scholar.google.com/scholar?hl={params['hl']}&q={params['q']}",
# }
#
#
# def cite_ids() -> list:
#     response = requests.get("https://scholar.google.com/scholar", params=params, headers=headers)
#     soup = Selector(response.text)
#
#     # returns a list of publication ID's -> U8bh6Ca9uwQJ
#     return soup.xpath("//*[contains(concat(' ',normalize-space(@class),' '),' gs_or ')]//@data-cid").getall()
#
# def scrape_cite_results() -> list:
#     cited_authors = []
#
#     for cite_id in cite_ids():
#         response = requests.get(f"https://scholar.google.com/scholar?output=cite&q=info:{cite_id}:scholar.google.com", headers=headers, proxies=proxies)
#         soup = Selector(response.text)
#
#         for result in soup.css("tr"):
#             institution = result.xpath("th/text()").get()
#             authors = result.xpath("td/text()").get()
#
#             cited_authors.append({"institution": institution, "cited_authors": authors})
#
#     return cited_authors
#
# print(json.dumps(scrape_cite_results(), indent=2))

import os, json
from serpapi import GoogleSearch


def organic_results() -> list[str]:
    params = {
        "api_key": os.getenv("API_KEY"),
        "engine": "google_scholar",
        "q": "automated container terminal",  # search query
        "hl": "en"                            # language
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    return [result["result_id"] for result in results["organic_results"]]


def cite_results() -> list[dict[str]]:

    citation_results = []

    for citation_id in organic_results():
        params = {
            "api_key": os.getenv("API_KEY"),
            "engine": "google_scholar_cite",
            "q": citation_id
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        for result in results["citations"]:
            if "APA" in result["title"]:
                institution = result["title"]
                authors = result["snippet"]

                citation_results.append({
                    "institution": institution,
                    "authors": authors
                })

    return citation_results

print(json.dumps(cite_results(), indent=2))