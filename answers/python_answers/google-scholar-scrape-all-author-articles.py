from parsel import Selector
import requests, json, os

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
params = {
    "q": "samsung",
    "hl": "en",
    "gl": "us"
}

# https://2.python-requests.org/en/master/user/advanced/#proxies
proxies = {
    "http": "http://2CH8vhoXpDouoog:xMqL4guJQ8yjnlq@server.proxyland.io:9090"
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

html = requests.get("URL", params=params, headers=headers, proxies=proxies, timeout=30)
selector = Selector(html.text)
