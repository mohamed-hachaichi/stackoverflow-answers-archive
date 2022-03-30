If you try to print the text of the current selector, then the user will get the combined text from the child selectors and the current selector together. To solve this problem, a loop was used that allows you to remove the text from the child selectors and leave only the text of the current selector.

Code and [full example in online IDE](https://replit.com/@chukhraiartur/how-to-retrieve-yahoo-search-results#main.py):

```python
from bs4 import BeautifulSoup
import requests, lxml

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "p": "deep"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

html = requests.get("https://search.yahoo.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

for result in soup.select(".compTitle.options-toggle"):
    url = result.select_one("a")["href"]
    text = list(result.select_one("a").text)

    for i in range(len(result.select_one("span").text)):
        text.pop(0)
        
    print("".join(text), url, sep="\n")
```

Output:

```lang-none
DeepL Translate: The world's most accurate translator
https://r.search.yahoo.com/_ylt=Awr9GjGgZERiFfEANhtXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1648678176/RO=10/RU=https%3a%2f%2fwww.deepl.com%2ftranslator/RK=2/RS=TVz6fqq87B12oa7dLig44PkzAJs-
... other results
```
____

There is no method in the BeautifulSoup library that allows you to take the text of a given selector without using the text of the child selectors. Therefore, it was decided to use the Parsel library, which has it.

Using [`parsel`](https://parsel.readthedocs.io/en/latest/):

```python
from parsel import Selector
import requests

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "p": "deep"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

html = requests.get("https://search.yahoo.com/search", params=params, headers=headers, timeout=30)
soup = Selector(text=html.text)

for result in soup.css(".compTitle.options-toggle"):
    url = result.css("a::attr(href)").get()
    text = result.css("h3 > a::text").get()
    print(text, url, sep="\n")
```

Output:

```lang-none
DeepL Translate: The world's most accurate translator
https://r.search.yahoo.com/_ylt=Awr9GjGgZERiFfEANhtXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3Ny/RV=2/RE=1648678176/RO=10/RU=https%3a%2f%2fwww.deepl.com%2ftranslator/RK=2/RS=TVz6fqq87B12oa7dLig44PkzAJs-
... other results
```
____

Alternatively, you can use [Yahoo! Organic Results API](https://serpapi.com/yahoo-organic-results) from SerpApi. It`s a paid API with the free plan.

The difference is that it will process blocks from Yahoo or other search engines, so the end user doesn't have to write full code, but only needs to think about what data to retrieve.

Example code to integrate:

```python
from serpapi import YahooSearch
import os

params = {
  "api_key": os.getenv("API_KEY"),
  "engine": "yahoo",
  "p": "deep"
}

search = YahooSearch(params)
results = search.get_dict()

for result in results["organic_results"]:
    print(result["title"], result["link"], sep="\n")
```

Output:

```lang-none
DeepL Translate: The world's most accurate translator
https://www.deepl.com/translator
Deep Definition & Meaning - Merriam-Webster
https://www.merriam-webster.com/dictionary/deep
460 Synonyms & Antonyms of DEEP - Merriam-Webster
https://www.merriam-webster.com/thesaurus/deep
Deep Definition & Meaning | Dictionary.com
https://www.dictionary.com/browse/deep
Online Service - Connecticut
https://portal.ct.gov/DEEP/Online-Services/Online-Services-Home
```

> Disclaimer, I work for SerpApi.