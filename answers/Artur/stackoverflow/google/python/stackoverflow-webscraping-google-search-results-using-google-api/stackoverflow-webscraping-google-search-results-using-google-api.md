Your code is constantly iterating over the first element. This is because you are not using a `i` - loop local variable.

The [`for` statement](https://docs.python.org/3/tutorial/controlflow.html#for-statements) in Python can iterate over the elements of any sequence in the order they appear in the sequence (list or string). If you need to iterate over a sequence of numbers, the [`range()` built-in function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function) comes in handy.

I used the second option with the `range()` function, where the variable `i` was used as the iteration number, which corresponds to the indices in the resulting array of values ​​and allows each iteration to output a new value at the index. The [`len()` built-in function](https://docs.python.org/3/library/functions.html#len) is used to count the number of elements in a sequence and return the number to the `range()` function, thus passing in how many times the loop should be iterated.

Below is a modified snippet of your code:

```python
# your code

for i in range(len(results)):
    print(f"Title == {results['items'][i]['title']}")
    print(f"Link == {results['items'][i]['link']}")
    snippet = results['items'][i]['snippet'].replace('\n', "")
    html_snippet = results['items'][i]['htmlSnippet'].replace('\n', "")
    html_snippet = html_snippet.replace("<b>", "")
    html_snippet = html_snippet.replace("</b>", "")
    html_snippet = html_snippet.replace("<br>", "")
    html_snippet = html_snippet.replace("&nbsp;…", ".")
    print(f"Description == {snippet}{html_snippet}", end="\n\n")
```

Variant that does the same but using only the [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/) library:

```python
# variant using only the Beautiful Soup library 

for result in soup.select(".tF2Cxc"):
    title = f'Title: {result.select_one("h3").text}'
    link = f'Link: {result.select_one("a")["href"]}'
    description = f'Description: {result.select_one(".VwiC3b").text}'

    print(title, link, description, sep="\n", end="\n\n")
```

I decided to present an option using only the `Beautiful Soup` library, since your code uses a lot of libraries that you can do without. I also noticed that you manually remove the tags, although this can be done more easily by selecting the text of the `topmost selector`. This will ignore the inner tags and take their contents.

![An illustration of what to get](https://res.cloudinary.com/dqfrazolx/image/upload/v1650404120/images/VwiC3b_kwe17k.png)

Also, make sure you're using [request headers](https://docs.python-requests.org/en/master/user/quickstart/#custom-headers) [`user-agent`](https://developer.mozilla.org/en-US/docs/Glossary/User_agent) to act as a "real" user visit. Because default `requests` `user-agent` is [`python-requests`](https://github.com/psf/requests/blob/589c4547338b592b1fb77c65663d8aa6fbb7e38b/requests/utils.py#L808-L814) and websites understand that it's most likely a script that sends a request. [Check what's your `user-agent`](https://www.whatismybrowser.com/detect/what-is-my-user-agent/).

Added [`f-string` is a pythonic way of concatenating strings](https://docs.python.org/3.6/reference/lexical_analysis.html#formatted-string-literals) that looks cleaner. 

Code and [full example in online IDE](https://replit.com/@chukhraiartur/stackoverflow-webscraping-google-search-results-using-google#main.py):

```python
import sys
import urllib.request
import urllib.parse
import re
from urllib.request import urlopen as ureqs
from bs4 import BeautifulSoup as soup
from googleapiclient.discovery import build

# Google Personal Search Engine information
my_api_key = <key>
my_cse_id = <id>

# Google Search
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


# Setting up so that user can input query
query = input("Enter the query:\n")

# Getting into printing the results
results = google_search(query, my_api_key, my_cse_id)

print("\n*********Google Search Results*********\n")

for i in range(len(results)):
    print(f"Title == {results['items'][i]['title']}")
    print(f"Link == {results['items'][i]['link']}")
    snippet = results['items'][i]['snippet'].replace('\n', "")
    html_snippet = results['items'][i]['htmlSnippet'].replace('\n', "")
    html_snippet = html_snippet.replace("<b>", "")
    html_snippet = html_snippet.replace("</b>", "")
    html_snippet = html_snippet.replace("<br>", "")
    html_snippet = html_snippet.replace("&nbsp;…", ".")
    print(f"Description == {snippet}{html_snippet}", end="\n\n")
```

Output:

```lang-none
*********Google Search Results*********

Title == Coffee - Wikipedia
Link == https://en.wikipedia.org/wiki/Coffee
Description == Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain flowering plants in the Coffea genus. From the coffee fruit, ...Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain flowering plants in the Coffea genus. From the coffee fruit,&nbsp;...

Title == Starbucks Coffee Company
Link == https://www.starbucks.com/
Description == More than just great coffee. Explore the menu, sign up for Starbucks® Rewards, manage your gift card and more.More than just great coffee. Explore the menu, sign up for Starbucks® Rewards, manage your gift card and more.

... other results
```
____

Using [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/):

```python
from bs4 import BeautifulSoup
import requests, lxml

query = input("Enter the query:\n")

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": query,
    "hl": "en",  # language
    "gl": "us"   # country of the search, US -> USA
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

for result in soup.select(".tF2Cxc"):
    title = f'Title: {result.select_one("h3").text}'
    link = f'Link: {result.select_one("a")["href"]}'
    description = f'Description: {result.select_one(".VwiC3b").text}'

    print(title, link, description, sep="\n", end="\n\n")
```

Output:

```lang-none
Title: Coffee - Wikipedia
Link: https://en.wikipedia.org/wiki/Coffee
Description: Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain flowering plants in the Coffea genus. From the coffee fruit, ...

Title: Starbucks Coffee Company
Link: https://www.starbucks.com/
Description: More than just great coffee. Explore the menu, sign up for Starbucks® Rewards, manage your gift card and more.

... other results
```
____

Alternatively, you can use [Google Organic Results API](https://serpapi.com/organic-results) from SerpApi. It`s a paid API with the free plan.

The difference is that it will bypass blocks from Google or other search engines, so the end-user doesn't have to figure out how to do it, maintain the parse, and only think about what data to retrieve instead.

Example code to integrate:

```python
from serpapi import GoogleSearch
import os

query = input("Enter the query:\n")

params = {
  # https://docs.python.org/3/library/os.html#os.getenv
  "api_key": os.getenv("API_KEY"),  # your serpapi api key
  "engine": "google",               # search engine
  "q": query                        # search query
  # other parameters
}

search = GoogleSearch(params)  # where data extraction happens on the SerpApi backend
results = search.get_dict()    # JSON -> Python dict

for result in results["organic_results"]:
    print(result["title"], result["link"], result["snippet"], sep="\n", end="\n\n")
```

Output:

```lang-none
Coffee - Wikipedia
https://en.wikipedia.org/wiki/Coffee
Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain flowering plants in the Coffea genus. From the coffee fruit, ...

Starbucks Coffee Company
https://www.starbucks.com/
More than just great coffee. Explore the menu, sign up for Starbucks® Rewards, manage your gift card and more.

... other results
```

> Disclaimer, I work for SerpApi.