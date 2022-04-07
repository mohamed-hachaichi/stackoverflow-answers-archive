# https://stackoverflow.com/questions/67138092/stopiteration-error-while-using-scholarly-pprint-function

from scholarly import scholarly
from serpapi import GoogleScholarSearch
import json

professor_list = ["Marty Banks, Berkeley",
                  "Adam Lobel, Blizzard",
                  "Daniel Blizzard, Blizzard",
                  "Shuo Chen, Blizzard",
                  "Ian Livingston, Blizzard",
                  "Minli Xu, Blizzard"]

# professor_results = []
#
# for professor_name in professor_list:
#     for professor_result in scholarly.search_author(name=professor_name):
#         professor_results.append({
#             "name": professor_result.get("name"),
#             "affiliations": professor_result.get("affiliation"),
#             "email_domain": professor_result.get("email_domain"),
#             "interests": professor_result.get("interests"),
#             "citedby": professor_result.get("citedby")
#         })
#
# print(json.dumps(professor_results, indent=2, ensure_ascii=False))

# for professor_name in professor_list:
#     search_query = scholarly.search_author(name=professor_name)
#     scholarly.pprint(next(search_query, None))

# ----------------------------------------------------------------------

for professor_name in professor_list:
    params = {
        "api_key": "Your SerpApi API key",
        "engine": "google_scholar_profiles",
        "hl": "en",
        "mauthors": professor_name
    }

    search = GoogleScholarSearch(params)
    results = search.get_dict()

    for result in results["profiles"]:
        print(json.dumps(result, indent=2))
