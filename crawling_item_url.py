import requests
from bs4 import BeautifulSoup
import time

# 크롤링한 정보를 저장할 파일 열기
file = open(
    './올리브영/홈_프래그런스.txt', 'w'
)

# url 정보 중 페이지 넘버에 대한 value를 for 문으로 순회
for i in range(1, 8):
    url = 'https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100050008&fltDispCatNo=&prdSort=01&pageIdx={}&rowsPerPage=100'.format(
        i)

    response = requests.get(url)

    # 요청에 대한 값이 200(정상)인 경우 동작
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # "a" 태그의 "prd_thumb" 클래스를 모두 찾음
        for item in soup.find_all('a', 'prd_thumb'):
            # 찾은 클래스에 포함된 "href" 만 url 변수에 저장
            url = item.attrs['href']
            file.write(url)
            file.write('\n')

    else:
        print(response.status_code)
