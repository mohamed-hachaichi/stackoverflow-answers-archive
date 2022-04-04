If you try to print the text of the current selector, you will get the combined text of the child `<span>` element as well, which is not what you want. To do that, you can use the `h3 > a` selector.

![An illustration of what to get](https://user-images.githubusercontent.com/78694043/161210494-66af1690-382b-43d4-a919-3fb698b272a9.png)

However, when using BeautifulSoup, CSS selector's behavior could be weird, for example:

```python
# bs4

for result in soup.select(".compTitle.options-toggle"):
        text = result.select_one("h3 > a").text
        print(text)
 
#                                                     👇      👇      👇                          
# www.merriam-webster.com › dictionary › deepDeep Definition & Meaning - Merriam-Webster
```
```python
# parsel

for result in soup.css(".compTitle.options-toggle"):
        text = result.css("h3 > a::text").get()
        print(text)

# Deep Definition & Meaning - Merriam-Webster
```
This could be because [`parsel` translates every CSS selector query to XPath](https://github.com/scrapy/parsel/blob/f5f73d34ba787ad0c9df25de295de6e196ecd91d/parsel/selector.py#L350-L351) but I'm not sure what is causing such behavior in BeautifulSoup.

Also, make sure you're using [request headers](https://docs.python-requests.org/en/master/user/quickstart/#custom-headers) [`user-agent`](https://developer.mozilla.org/en-US/docs/Glossary/User_agent) to act as a "real" user visit. Because default `requests` `user-agent` is [`python-requests`](https://github.com/psf/requests/blob/589c4547338b592b1fb77c65663d8aa6fbb7e38b/requests/utils.py#L808-L814) and websites understand that it's most likely a script that sends a request. [Check what's your `user-agent`](https://www.whatismybrowser.com/detect/what-is-my-user-agent/).

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

The difference is that it will bypass blocks from Yahoo! or other search engines, so the end-user doesn't have to figure out how to do it, maintain the parse, and only think about what data to retrieve instead.

Example code to integrate:

```python
from serpapi import YahooSearch
import os

# You must enter your API_KEY
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