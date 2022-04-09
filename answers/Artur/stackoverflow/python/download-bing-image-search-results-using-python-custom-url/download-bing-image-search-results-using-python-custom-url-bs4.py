# https://stackoverflow.com/questions/52015361/download-bing-image-search-results-using-python-custom-url
# https://replit.com/@chukhraiartur/download-bing-image-search-results-using-python-custom-url#main.py


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
