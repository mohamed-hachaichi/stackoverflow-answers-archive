import requests, re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4664.45 Safari/537.36",
}

params = {
    "to":"2021-11-29T09:15:00.000Z",
    "limit":"321",
    "lpAddress":"0xd8b6A853095c334aD26621A301379Cc3614f9663",
    "interval":"15m",
    "baseLp":"0x58F876857a02D6762E0101bb5C46A8c1ED44Dc16"
}



# https://poocoin.app/api2/candles-bsc?data=[YmLNHK6TU[Kblm4UXqKeF2FTYSSW2KsZ32XfnO6TU[KblJ1UVeONWKGSYebblF{U2S[fWqIVYeObmVzXYqCN1:VTUCQSGmOWHiWUVSkOl27WU[OSFG2UVSCe2eqTYOKcYixZmetNFmrc4qOblG{TX25e2GYVnukcW[7Z4mKOlmrRkSbSHiqUnuGOF6VUYeQWG[rUYqONGmWVYmPbmm6UWWGfl2FSYqPfnyFXYqONl2VVn2QWGlzUYmKd1mucIWlS2[6[H2Hd1mrc3mOWG[1TXm4bWmuSoqbWYi4TXqwbV2J[{GQSWl1Uoq[OF6V[HiOSFqGUnqkNl2sWYeOWFG5XX2KNWG7VUKSWHirUWWXSV6FVlW[flVzTX5xQR%3E%3E
# https://poocoin.app/api2/candles-bsc?data=[YmLNHK6TU[Kblm4UXqKeF2FTYSSW2KsZ32XfnO6TU[KblJ1UVeONWKGSYebblF{U2S[fWqIVYeObmVzXYqCN1:VTUCQSGmOWHiWUVSkOl27WU[OSFG2UVSCe2eqTYOKcYixZmetNFmrc4qOSFW{TX25e2GYVnukcW[7Z4mKOlmrRkSPfnSuUoqsfGG7cH2Pb111UlWOfV6rUnmOW2m6UWSLRl2GVYqTSHStUWWPSV:V[{GPSGqEUVOKd1mucIWlS2[6[H2Hd1mrc3mOWG[1TXm4bWmuSoqbWYi4TXqwbV2J[{GQSWl1Uoq[OF6V[HiOSFqGUnqkNl2sWYeOWFG5XX2KNWG7VUKSWHirUWWXSV6FVlW[flVzTX5xQR%3E%3E

# response = requests.get("https://api2.poocoin.app/candles-bsc", params=params, headers=headers)
response = requests.get("https://poocoin.app/api2/candles-bsc", headers=headers)
print(response)

# whole response from API call for a particular token (i believe)
# some data needs to be adjusted (open/close price, etc.)
# for result in response:
#     count = result["count"]
#     _time = result["time"]
#     open_price = result["open"]
#     close_price = result["close"]
#     high = result["high"]
#     low = result["low"]
#     volume = result["volume"]
#     base_open = result["baseOpen"]
#     base_close = result["baseClose"]
#     base_high = result["baseHigh"]
#     base_low = result["baseLow"]
#
#     print(f"{count}\n"
#           f"{_time}\n"
#           f"{open_price}\n"
#           f"{close_price}\n"
#           f"{high}\n"
#           f"{low}\n"
#           f"{volume}\n"
#           f"{base_open}\n"
#           f"{base_close}\n"
#           f"{base_high}\n"
#           f"{base_low}\n")