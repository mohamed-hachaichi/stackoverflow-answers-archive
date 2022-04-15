from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import json

params = {
  "api_key": "your serpapi_api_key",
  "engine": "google",
  "q": "tesla",
  "num": "100"
}

search = GoogleSearch(params)

organic_results_data = []
page_num = 0

organic_results_is_present = True
while organic_results_is_present:
    results = search.get_dict()
    
    page_num += 1
    
    for result in results["organic_results"]:
        organic_results_data.append({
            "page_num": page_num,
            "position": result.get("position"),
            "title": result.get("title"),
            "link": result.get("link"),
            "displayed_link": result.get("displayed_link")
        })
    
    if "next_link" in results.get("serpapi_pagination", []):
            search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next_link")).query)))
    else:
        organic_results_is_present = False
    
    
print(json.dumps(organic_results_data, indent=2, ensure_ascii=False))
