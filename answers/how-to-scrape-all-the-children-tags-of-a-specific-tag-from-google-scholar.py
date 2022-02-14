# https://stackoverflow.com/questions/54377479/how-to-scrape-all-the-children-tags-of-a-specific-tag-from-google-scholar-websi
# https://replit.com/@DimitryZub1/How-to-scrape-all-the-children-tags-of-a-specific-tag#main.py

from parsel import Selector
from bs4 import BeautifulSoup
import requests, lxml

params = {
    "user": "zD0vtfwAAAAJ",
    "citation_for_view": "zD0vtfwAAAAJ:d1gkVwhDpl0C",
    "hl": "en",
    "view_op": "view_citation"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
}

html = requests.get("https://scholar.google.com.au/citations", params=params, headers=headers, timeout=30)
soup, selector = BeautifulSoup(html.text, "lxml"), Selector(html.text)

# using parsel
co_authors = selector.css(".gs_scl:nth-child(1) .gsc_oci_value::text").getall()
print(co_authors)

# or using beautifulsoup
bs4_co_authors = [co_author.text for co_author in soup.select(".gs_scl:nth-child(1) .gsc_oci_value")]
print(bs4_co_authors)
