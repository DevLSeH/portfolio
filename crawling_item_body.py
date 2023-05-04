import time
import os
import re
import requests
from bs4 import BeautifulSoup

# "./상품" 폴더 안의 모든 파일을 순회함
for (root, directories, files) in os.walk('./올리브영'):
    for file in files:
        file_path = os.path.join(root, file)
        # crawling_item_url 에서 저장한 상품 url.txt 파일을 연다
        f = open(file_path, 'r')

        for url in f:

            response = requests.get(url)
            try:
                if response.status_code == 200:
                    html = response.text
                    soup = BeautifulSoup(html, 'html.parser')

                    # 브랜드 이름을 저장한다
                    item_brand = soup.find('a', id='moveBrandShop')
                    item_brand = item_brand.text
                    print(item_brand)

                    # 상품 이름을 저장한다
                    item_name = soup.find('p', 'prd_name')
                    item_name = item_name.text
                    print(item_name)

                    # 상품 가격을 저장한다
                    item_prices = soup.find('span', 'price-2')
                    item_price = item_prices.text.replace('\n', '')
                    print(item_price)

                    # 상품 이름을 정제한다. 정제 방식은 replace 외에 더 편한 방식이 있으니 변경해도 좋다
                    dirname = file.replace('.txt', '')
                    dirpath = './상품/{}'.format(dirname)
                    name = item_name.replace(' ', '_').replace(
                        '/', '').replace('*', '').replace('[', '').replace(']', '').replace('!', '').replace(
                        '\\', '').replace('.', '').replace('\t', '')

                    # 상품 이름으로 생성된 폴더가 없다면 만든다
                    if not os.path.isdir(dirpath):
                        os.makedirs(dirpath)

                    save = open('./상품/{0}/{1}.txt'.format(dirname,
                                name), 'a', encoding='UTF-8')

                    save.write(item_brand)
                    save.write('\n')
                    save.write(item_name)
                    save.write('\n')
                    save.write(item_price)
                    save.write('\n')

                    item_main_pic = soup.find('img', id='mainImg')['src']
                    print(item_main_pic)
                    save.write(item_main_pic)

                    # 올리브영 웹페이지의 특이성으로 내부 순회가 필요하다
                    item_pic = soup.select(
                        '.contEditor img')
                    for i in range(0, len(item_pic)):
                        if (item_pic[i]):
                            img = item_pic[i]['src']
                            print(img)
                            save.write(img)
                            save.write('\n')
                        else:
                            break

                else:
                    print(response.status_code)
            except:
                exception = open('./exception.txt', 'w')
                exception.write(item_name)
                exception.write('\n')
