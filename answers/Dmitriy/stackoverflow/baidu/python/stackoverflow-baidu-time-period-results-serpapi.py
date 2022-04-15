from serpapi import BaiduSearch
import json

params = {
  "api_key": "your serpapi api key",
  "engine": "baidu",
  "q": "Coffee",
  "lm": "7"
}

search = BaiduSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(json.dumps(result, indent=2, ensure_ascii=False))