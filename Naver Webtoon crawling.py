from bs4 import BeautifulSoup
import requests
import shutil
import os
import sys

with open("sample.html", "wb+") as f:
    inputSearch = "388"
    fullUrl = 'https://comic.naver.com/webtoon/detail.nhn?titleId=183559&no=' + inputSearch + '&weekday = mon'
    r = requests.get(fullUrl)
    html = r.text
    f.write(html.encode("utf-8"))
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select('#comic_view_area > div.wt_viewer > img')
    directory = os.path.dirname('./img/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(len(my_titles)):
        img = soup.find("img", {'id': "content_image_" + str(i)})
        img_src = img.get("src")
        img_name = str(i) + "pic"
        r = requests.get(img_src, stream=True, headers={'User-agent':
                                                            'Mozilla/5.0'})
        if r.status_code == 200:
            with open('./img/' + img_name + '.png', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
