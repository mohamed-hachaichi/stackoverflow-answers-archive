# https://stackoverflow.com/questions/66996354/web-scraping-multiple-google-scholar-pages-in-python
# https://replit.com/@DimitryZub1/web-scraping-multiple-google-scholar-pages-in-python#bs4_solution.py


from bs4 import BeautifulSoup
import requests, lxml, json, os, re
import pandas as pd
from serpapi import GoogleSearch


def bs4_scrape_multiple_authors():
    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    }

    # https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
    authors_df = pd.read_excel("google_scholar_scrape_multiple_authors.xlsx", sheet_name="authors")  # sheet_name is optional in this case

    # returns a list of author links
    for author_link in authors_df["author_link"].to_list():
        html = requests.get(author_link, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, "lxml")

        print(f"Currently extracting: {soup.select_one('#gsc_prf_in').text}")

        author_image = f'https://scholar.google.com{soup.select_one("#gsc_prf_pup-img")["src"]}'
        author_email = soup.select_one("#gsc_prf_ivh").text

        print(author_image, f"Author email: {author_email}", sep="\n")

        for article in soup.select("#gsc_a_b .gsc_a_t"):
            article_title = article.select_one(".gsc_a_at").text
            article_link = f'https://scholar.google.com{article.select_one(".gsc_a_at")["href"]}'
            article_authors = article.select_one(".gsc_a_at+ .gs_gray").text
            article_publication = article.select_one(".gs_gray+ .gs_gray").text

            print(article_title,
                  article_link,
                  article_authors,
                  article_publication, sep="\n")

        print("-" * 15)


def serpapi_scrape_multiple_authors():
    authors_df = pd.read_excel("google_scholar_scrape_multiple_authors.xlsx", sheet_name="authors")  # sheet_name is optional in this case

    for author in authors_df["author_link"].to_list():
        params = {
            "api_key": os.getenv("API_KEY"),
            "engine": "google_scholar_author",
            "hl": "en",
            "author_id": re.search(r"user=(.*)", author).group(1)  # -> VxOmZDgAAAAJ, unique author ID from the URL
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        print(f"Extracting data from: {results['author']['name']}\n"
              f"Author info: {results['author']}\n\n"
              f"Author articles:\n{results['articles']}\n")

bs4_scrape_multiple_authors()
