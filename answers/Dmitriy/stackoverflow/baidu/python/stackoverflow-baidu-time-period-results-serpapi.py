from serpapi import BaiduSearch
import json

params = {
  "api_key": "d690f858b1cfbfab3dd81f1947768ac3abe58c6620c00fdb0835b41b5ece525f",
  "engine": "baidu",
  "q": "Coffee",
  "lm": "7"
}

search = BaiduSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(json.dumps(result, indent=2, ensure_ascii=False))