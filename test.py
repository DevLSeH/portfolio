import requests
from bs4 import BeautifulSoup
import time
import os
import re

url = 'https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000174279&dispCatNo=100000100100002&trackingCd='
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

img = soup.find('img', id='mainImg')['src']
print(img)
