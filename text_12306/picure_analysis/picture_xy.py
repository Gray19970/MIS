# -*- coding: utf-8 -*-
# name=Gray_jiang
# version=python3.7
import requests
from bs4 import BeautifulSoup
def get_pic_xy(picture):
    url = 'http://littlebigluo.qicp.net:47720/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    files = {'pic_xxfile': (picture, open(picture, 'rb'), 'image/png')}
    html=requests.post(url=url, files=files)
    soup=BeautifulSoup(html.text,'lxml')
    answer=soup.find('b')
    list_answer=[]
    for i in answer.get_text():
        if i.isdigit():
            list_answer.append(i)
    return list_answer
if __name__ == '__main__':
    a=get_pic_xy('11.jpg')
    print(a)