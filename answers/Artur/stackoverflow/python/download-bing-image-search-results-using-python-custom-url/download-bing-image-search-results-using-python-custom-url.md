To get the URL of an image, you can query and get the URL of the site where the images are located. After that, make requests to these sites and get the URLs of the images.

But you can make things easier. Bing uses a special `"m" attribute` in link selectors that stores the [`JSON format`](https://docs.python.org/3/library/json.html) and the image URL is stored in the `"murl" key`.

![Demonstration of uploading files to a folder](https://user-images.githubusercontent.com/81998012/161598302-80ba9b28-6656-4656-a0d5-a6f7188ce0dc.gif)

To download all images locally to your computer, you can use 2 methods:

```python
# bs4

for index, url in enumerate(soup.select(".iusc"), start=1):
    img_url = json.loads(url["m"])["murl"]
    image = requests.get(img_url, headers=headers, timeout=30)
    query = query.lower().replace(" ", "_")
    
    if image.status_code == 200:
        with open(f"images/{query}_image_{index}.jpg", 'wb') as file:
            file.write(image.content)
```

```python
# urllib

for index, url in enumerate(soup.select(".iusc"), start=1):
    img_url = json.loads(url["m"])["murl"]
    query = query.lower().replace(" ", "_")

    opener = req.build_opener()
    opener.addheaders=[("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36")]
    req.install_opener(opener)
    req.urlretrieve(img_url, f"images/{query}_image_{index}.jpg")
```

In the first case, a [built-in language feature](https://docs.python.org/3/library/functions.html#open) was used to load the image locally. In the second case, the [`urlretrieve method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve) of the [`urllib.request library`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) was used.

Also, make sure you're using [request headers](https://docs.python-requests.org/en/master/user/quickstart/#custom-headers) [`user-agent`](https://developer.mozilla.org/en-US/docs/Glossary/User_agent) to act as a "real" user visit. Because default `requests` `user-agent` is [`python-requests`](https://github.com/psf/requests/blob/589c4547338b592b1fb77c65663d8aa6fbb7e38b/requests/utils.py#L808-L814) and websites understand that it's most likely a script that sends a request. [Check what's your `user-agent`](https://www.whatismybrowser.com/detect/what-is-my-user-agent/).

An error might occur with URLs where you have to verify a captcha or when the link returns an unsuccessful [`HTTP status code`](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

___

Code and [full example in online IDE](https://replit.com/@chukhraiartur/how-to-retrieve-yahoo-search-results#main.py):

```python
from bs4 import BeautifulSoup
import requests, lxml, json

query = "sketch using iphone students"

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": query,
    "first": 1
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

response = requests.get("https://www.bing.com/images/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(response.text, "lxml")

for index, url in enumerate(soup.select(".iusc"), start=1):
    img_url = json.loads(url["m"])["murl"]
    image = requests.get(img_url, headers=headers, timeout=30)
    query = query.lower().replace(" ", "_")
    
    if image.status_code == 200:
        with open(f"images/{query}_image_{index}.jpg", 'wb') as file:
            file.write(image.content)
```
____

Using [`urlretrieve`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve).

```python
from bs4 import BeautifulSoup
import requests, lxml, json
import urllib.request as req

query = "sketch using iphone students"

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": query,
    "first": 1
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

response = requests.get("https://www.bing.com/images/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(response.text, "lxml")

for index, url in enumerate(soup.select(".iusc"), start=1):
    img_url = json.loads(url["m"])["murl"]
    query = query.lower().replace(" ", "_")

    opener = req.build_opener()
    opener.addheaders=[("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36")]
    req.install_opener(opener)
    req.urlretrieve(img_url, f"images/{query}_image_{index}.jpg")
```
