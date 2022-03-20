# https://stackoverflow.com/questions/21839877/using-beautiful-soup-to-clean-up-scraped-html-from-scrapy
# https://replit.com/@DimitryZub1/using-beautiful-soup-to-clean-up-scraped-html-from-scrapy#main.py

import scrapy

class ScholarSpider(scrapy.Spider):
    name = "scholar_titles"
    allowed_domains = ["scholar.google.com"]
    start_urls = ["https://scholar.google.com/scholar?q=intitle%3Apython+xpath"]

    def parse(self, response):
        for quote in response.xpath('//*[@class="gs_rt"]/a'):
            yield {
                "title": quote.xpath("normalize-space()").get()
            }

from serpapi import GoogleScholarSearch

params = {
  "api_key": "Your SerpApi API key",
  "engine": "google_scholar",   # parsing engine
  "q": "intitle:python_answers xpath",  # search query
  "hl": "en"                    # language
}

search = GoogleScholarSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    title = result["title"]
    print(title)