from bs4 import BeautifulSoup
import requests, lxml

params = {
    "q": "samsung",
    "hl": "en"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
    "server": "scholar",
    "referer": f"https://scholar.google.com/scholar?hl={params['hl']}&q={params['q']}",
}


def cite_ids() -> list:
    response = requests.get("https://scholar.google.com/scholar", params=params, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "lxml")

    # returns a list of publication ID's -> U8bh6Ca9uwQJ
    return [result["data-cid"] for result in soup.select(".gs_or")]


def scrape_cite_results() -> list:
    bibtex_data = []

    for cite_id in cite_ids():
        response = requests.get(f"https://scholar.google.com/scholar?output=cite&q=info:{cite_id}:scholar.google.com", headers=headers,
                                timeout=10)
        soup = BeautifulSoup(response.text, "lxml")

        # selects first matched element which in this case always will be BibTeX
        # if Google will not switch BibTeX position.
        bibtex_data.append(soup.select_one(".gs_citi")["href"])

    # returns a list of BibTex URLs, for example: https://scholar.googleusercontent.com/scholar.bib?q=info:ifd-RAVUVasJ:scholar.google.com/&output=citation&scisdr=CgVDYtsfELLGwov-iJo:AAGBfm0AAAAAYgD4kJr6XdMvDPuv7R8SGODak6AxcJxi&scisig=AAGBfm0AAAAAYgD4kHUUPiUnYgcIY1Vo56muYZpFkG5m&scisf=4&ct=citation&cd=-1&hl=en
    return bibtex_data