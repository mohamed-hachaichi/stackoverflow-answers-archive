# https://stackoverflow.com/questions/61586209/web-scraping-in-google-scholar-with-beautifulsoup-and-selenium-in-python
#

from parsel import Selector
import requests, json, os



def scrape_univ_profiles():
    params = {
        "mauthors": 'label:computer_vision "Michigan State University"|"U.Michigan"',
        "hl": "en",
        "view_op": "search_authors"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    }

    html = requests.get("https://scholar.google.com/citations", params=params, headers=headers, timeout=30)
    selector = Selector(html.text)

    profiles = []

    for profile in selector.css(".gs_ai_chpr"):
        profile_name = profile.css(".gs_ai_name a::text").get()
        profile_link = f'https://scholar.google.com{profile.css(".gs_ai_name a::attr(href)").get()}'
        profile_affiliation = profile.css('.gs_hlt::text').get()  # selects only university name without additional affiliation, e.g: Assistant Professor
        profile_email = profile.css(".gs_ai_eml::text").get()
        profile_interests = profile.css(".gs_ai_one_int::text").getall()

        profiles.append({
            "profile_name": profile_name,
            "profile_link": profile_link,
            "profile_affiliations": profile_affiliation,
            "profile_email": profile_email,
            "profile_interests": profile_interests
        })

    print(json.dumps(profiles, indent=2))

def serpapi_scrape_univ_profiles():
    from serpapi import GoogleSearch

    params = {
        "api_key": os.getenv("API_KEY"),
        "engine": "google_scholar_profiles",
        "hl": "en",
        "mauthors": 'label:computer_vision "Michigan State University"|"U.Michigan"'
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for profile in results["profiles"]:
        print(json.dumps(profile, indent=2))


