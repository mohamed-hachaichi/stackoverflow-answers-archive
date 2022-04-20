<p align="center">
  <img src="https://user-images.githubusercontent.com/78694043/162031042-8720f7d9-c3f2-4081-8358-976255e80fd2.png" />
</p>


## Folder structure naming convention

Rephrase the question to make it easier to search and understand.

```lang-none
<author>/
├─ <website_where_question_asked>/
│  ├─ <which_website_to_scrape>/
│  │  ├─ <which_language_used>/
│  │  │  ├─ <question_file_name>-<library_used>.<file_extension>

----------------------

dmitriy/
├─ stackoverflow/
│  ├─ google/
│  │  ├─ google_trends/
│  │  │  ├─ stackoverflow-scrape-google-trends-bs4.py
```

## Branch naming convention

Rephrase the question to make it easier to search and understand.

```lang-none
<website_where_question_asked>-<question>

Example:
stackoverflow-scrape-google-finance-time-series-bs4
twitter-scrape-google-trends
```

## File naming convention

Rephrase the question to make it easier to search and understand.

```lang-none
<website_where_question_asked>_<question>.<file_extension> 

stackoverflow_how_to_scrape_google_finance_time_series.py
twitter_how_to_scrape_google_trends.md
```

## Typical answer layout

<details><summary>👉 Stackoverflow and similar</summary>

- `.md` file that contains answer with code itself.
- `<any_programming_lang>` file with script code.

Answer file layout (`.md`):

```lang-none
# link to the question
# link to example in the online IDE (replit or similar)

# <explanation to the answer>
# ...
# <code>
# ... 
# (optional) <alternative API solution>
# ...
# <disclaimer> 
```

Script file layout (`<any_programming_lang>`): 

```lang-none
# <code>
# ...
# <alternative API solution>
```
</details>


<details><summary>👉 Twitter and similar</summary>

- `.md` file of the tweet.
- `<any_programming_lang>` file with script code that will be shared to online IDE.
- `GIF`/`Image`/`Video`

Tweet layout:

```lang-none
# <sentence> + <GIF/Image/Video>
```

Script file layout: 

```lang-none
# link to the question
# (optional, if needed) link to example in the online IDE (replit or similar)

# <code>
# ...
# <alternative API solution>
```
</details>

## Found an error/typo or something else to improve?

Two approaches:
1. Fork the repo and a pull request with an understandable explanation.
2. Open an issue with an understandable explanation.

Wait untill I or SerpApi member send you ❤️