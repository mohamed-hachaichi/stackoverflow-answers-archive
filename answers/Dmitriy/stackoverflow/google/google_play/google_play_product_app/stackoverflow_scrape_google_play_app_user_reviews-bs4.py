from bs4 import BeautifulSoup
import requests, lxml, re, json
from datetime import datetime

# user-agent headers to act as a "real" user visit
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

# search query params
params = {
    "id": "com.nintendo.zara",  # app name
    "gl": "ES"                  # country
}


html = requests.get("https://play.google.com/store/apps/details", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

# temporary store user comments
app_user_comments = []

# https://regex101.com/r/SrP5DS/1
app_user_reviews_data = re.findall(r"(\[\"gp.*?);</script>",
                                str(soup.select("script")), re.DOTALL)

for review in app_user_reviews_data:
    # https://regex101.com/r/M24tiM/1
    user_name = re.findall(r"\"gp:.*?\",\s?\[\"(.*?)\",", str(review))
    
    # https://regex101.com/r/TGgR45/1
    user_avatar = [avatar.replace('"', "") for avatar in re.findall(r"\"gp:.*?\"(https.*?\")", str(review))]

    # replace single/double quotes at the start/end of a string
    # https://regex101.com/r/iHPOrI/1
    user_comments = [comment.replace('"', "").replace("'", "") for comment in
                    re.findall(r"gp:.*?https:.*?]]],\s?\d+?,.*?,\s?(.*?),\s?\[\d+,", str(review))]

    # https://regex101.com/r/Z7vFqa/1
    user_comment_app_rating = re.findall(r"\"gp.*?https.*?\],(.*?)?,", str(review))
    
    # https://regex101.com/r/jRaaQg/1
    user_comment_likes = re.findall(r",?\d+\],?(\d+),?", str(review))
    
    # comment utc timestamp
    # use datetime.utcfromtimestamp(int(date)).date() to have only a date
    user_comment_date = [str(datetime.utcfromtimestamp(int(date))) for date in re.findall(r"\[(\d+),", str(review))]
    
    # https://regex101.com/r/GrbH9A/1
    user_comment_id = [ids.replace('"', "") for ids in re.findall(r"\[\"(gp.*?),", str(review))]
    
    for index, (name, avatar, comment, date, comment_id, likes, user_app_rating) in enumerate(zip(
        user_name,
        user_avatar,
        user_comments,
        user_comment_date,
        user_comment_id,
        user_comment_likes,
        user_comment_app_rating), start=1):

        app_user_comments.append({
            "position": index,
            "name": name,
            "avatar": avatar,
            "comment": comment,
            "app_rating": user_app_rating,
            "comment_likes": likes,
            "comment_published_at": date,
            "comment_id": comment_id
        })
        
print(json.dumps(app_user_comments, indent=2, ensure_ascii=False))
