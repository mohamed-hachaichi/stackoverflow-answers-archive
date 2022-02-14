# https://stackoverflow.com/questions/41325713/scrape-google-scholar-security-page

from parsel import Selector
import requests, json

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "label:security",
    "hl": "en",
    "view_op": "search_authors"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

html = requests.get("https://scholar.google.pl/citations", params=params, headers=headers, timeout=30)
selector = Selector(html.text)

profiles = []

for profile in selector.css(".gs_ai_chpr"):
    profile_name = profile.css(".gs_ai_name a::text").get()
    profile_link = f'https://scholar.google.com{profile.css(".gs_ai_name a::attr(href)").get()}'
    profile_email = profile.css(".gs_ai_eml::text").get()
    profile_interests = profile.css(".gs_ai_one_int::text").getall()

    profiles.append({
        "profile_name": profile_name,
        "profile_link": profile_link,
        "profile_email": profile_email,
        "profile_interests": profile_interests
    })

print(json.dumps(profiles, indent=2))