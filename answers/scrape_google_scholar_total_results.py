from serpapi import GoogleSearch

params = {
  "api_key": "Your SerpApi API key",
  "engine": "google_scholar",
  "q": "electronic knee",
  "hl": "it",
  "as_ylo": "2017"
}

search = GoogleSearch(params)
results = search.get_dict()

print(results["search_information"]["total_results"])

