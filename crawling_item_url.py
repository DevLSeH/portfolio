import requests
from bs4 import BeautifulSoup
import time

file = open(
    './올리브영/홈_프래그런스.txt', 'w'
)


for i in range(1, 8):
    url = 'https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100050008&fltDispCatNo=&prdSort=01&pageIdx={}&rowsPerPage=100'.format(
        i)

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('a', 'prd_thumb'):
            url = item.attrs['href']
            url_a = url
            file.write(url_a)
            file.write('\n')

    else:
        print(response.status_code)
