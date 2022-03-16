from serpapi import GoogleScholarSearch
import os

queries = ["moon",
           "pandas",
           "python",
           "data science",
           "ML",
           "AI",
           "animals",
           "amd",
           "nvidia",
           "intel",
           "asus",
           "robbery pi",
           "latex, tex",
           "amg",
           "blizzard",
           "world of warcraft",
           "cs go",
           "antarctica",
           "fifa",
           "amsterdam",
           "usa",
           "tesla",
           "economy",
           "ecology",
           "biology"]

for query in queries:
    params = {
        "api_key": os.getenv("API_KEY"),
        "engine": "google_scholar",
        "q": query,
        "hl": "en"
        }

    search = GoogleScholarSearch(params)
    results = search.get_dict()

    print(f"Extracting search query: {query}")

    for result in results["organic_results"]:
        print(result["title"])
