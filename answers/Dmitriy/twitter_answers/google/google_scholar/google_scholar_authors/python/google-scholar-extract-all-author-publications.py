import pandas as pd
from bs4 import BeautifulSoup
import requests, lxml, os

def scrape_all_authors_articles(author_id: str):
    params = {
        "user": author_id,   # user-id
        "hl": "en",          # language
        "gl": "us",          # country to search from
        "cstart": 0,         # articles page. 0 is the first page
        "pagesize": "100"    # articles per page
        }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
        }

    all_articles = []

    articles_is_present = True
    while articles_is_present:
        html = requests.post("https://scholar.google.com/citations", params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        for index, article in enumerate(soup.select("#gsc_a_b .gsc_a_t"), start=1):
            article_title = article.select_one(".gsc_a_at").text
            article_link = f'https://scholar.google.com{article.select_one(".gsc_a_at")["href"]}'
            article_authors = article.select_one(".gsc_a_at+ .gs_gray").text
            article_publication = article.select_one(".gs_gray+ .gs_gray").text

            print(article_title)

            all_articles.append({
                "title": article_title,
                "link": article_link,
                "authors": article_authors,
                "publication": article_publication
                })

        # this selector is checking for the .class that contains: "There are no articles in this profile."
        # example link: https://scholar.google.com/citations?user=VjJm3zYAAAAJ&hl=en&cstart=500&pagesize=100
        if soup.select_one(".gsc_a_e"):
            articles_is_present = False
        else:
            params["cstart"] += 100  # paginate to the next page

    pd.DataFrame(data=all_articles).to_csv(f"google_scholar_{params['user']}_articles.csv", encoding="utf-8", index=False)

user_ids = ["rUHfmpQAAAAJ", "HRkZPK4AAAAJ", "DubfkQ8AAAAJ", "VjJm3zYAAAAJ"]

for _id in user_ids:
    scrape_all_authors_articles(author_id=_id)
