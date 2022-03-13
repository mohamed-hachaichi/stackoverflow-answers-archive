# https://stackoverflow.com/questions/70033227/web-scraping-doi-with-beautifulsoup

from bs4 import BeautifulSoup
import requests, re, json

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

links = [
    "https://europepmc.org/api/get/articleApi?query=(EXT_ID:30980146%20AND%20SRC:med)&format=json&resultType=core",
    "https://ieeexplore.ieee.org/abstract/document/9599583"
]

data = []

for link in links:
    if "ieeexplore" in link:
        html = requests.get(link, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        # https://regex101.com/r/8vfYNp/1
        doi = json.loads(re.findall(r"xplGlobal\.document\.metadata=(.*?);", str(soup.select("script")))[0])["doi"]
        doi_link = json.loads(re.findall(r"xplGlobal\.document\.metadata=(.*?);", str(soup.select("script")))[0])["doiLink"]
        abstract = json.loads(re.findall(r"xplGlobal\.document\.metadata=(.*?);", str(soup.select("script")))[0])["abstract"]

        data.append({
            "parsed_url": link,
            "doi": doi,
            "doi_link": doi_link,
            "abstract": abstract,
        })
    else:
        html = requests.get(link, headers=headers, timeout=30).json()

        doi = html["resultList"]["result"][0]["doi"]
        doi_link = html["resultList"]["result"][0]["fullTextUrlList"]["fullTextUrl"][0]["url"]
        abstract = html["resultList"]["result"][0]["abstractText"]

        data.append({
            "parsed_url": link,
            "doi": doi,
            "doi_link": doi_link,
            "abstract": abstract,
        })

print(json.dumps(data, indent=2))
