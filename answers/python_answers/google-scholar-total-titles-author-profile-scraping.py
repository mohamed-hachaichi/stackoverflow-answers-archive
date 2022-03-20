import scrapy


class ScholarAuthorTitlesSpider(scrapy.Spider):
    name = 'google_scholar_author_titles'

    def scrapy_request(self):
        params = {
            "user": "cp-8uaAAAAAJ",  # user-id
            "hl": "en",  # language
            "gl": "us",  # country to search from
            "cstart": 0,  # articles page. 0 is the first page
            "pagesize": "100"  # articles per page
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
        }

        yield scrapy.Request(url="https://scholar.google.com/citations", method="GET", headers=headers, meta=params, callback=self.parse)

    # start_urls = ["https://scholar.google.com/citations?hl=en&user=_xwYD2sAAAAJ"]

    def parse(self, response):

        total_articles = []

        for index, article in enumerate(response.css("#gsc_a_b .gsc_a_t"), start=1):
            yield {
                "total_articles": index,
                "title": article.css(".gsc_a_at::text").get(),
                "link": f'https://scholar.google.com{article.css(".gsc_a_at::attr(href)").get()}',
                "authors": article.css(".gsc_a_at+ .gs_gray::text").get(),
                "publication": article.css(".gs_gray+ .gs_gray::text").get()
            }
