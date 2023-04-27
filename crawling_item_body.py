import requests
from bs4 import BeautifulSoup
import time
import os
import re

for (root, directories, files) in os.walk('./올리브영'):
    for file in files:
        file_path = os.path.join(root, file)
        f = open(file_path, 'r')

        for url in f:

            response = requests.get(url)
            try:
                if response.status_code == 200:
                    html = response.text
                    soup = BeautifulSoup(html, 'html.parser')

                    item_brand = soup.find('a', id='moveBrandShop')
                    item_brand = item_brand.text
                    print(item_brand)

                    item_name = soup.find('p', 'prd_name')
                    item_name = item_name.text
                    print(item_name)

                    item_prices = soup.find('span', 'price-2')
                    item_price = item_prices.text.replace('\n', '')
                    print(item_price)

                    dirname = file.replace('.txt', '')
                    dirpath = './상품/{}'.format(dirname)
                    name = item_name.replace(' ', '_').replace(
                        '/', '').replace('*', '').replace('[', '').replace(']', '').replace('!', '').replace(
                        '\\', '').replace('.', '').replace('\t', '')

                    if not os.path.isdir(dirpath):
                        os.makedirs(dirpath)

                    save = open('./상품/{0}/{1}.txt'.format(dirname,
                                name), 'a', encoding='UTF-8')

                    # save.write(item_brand)
                    # save.write('\n')
                    # save.write(item_name)
                    # save.write('\n')
                    # save.write(item_price)
                    # save.write('\n')

                    item_main_pic = soup.find('img', id='mainImg')['src']
                    print(item_main_pic)
                    save.write('\n MAIN IMG \n')
                    save.write(item_main_pic)

                    # item_pic = soup.select(
                    #     '.contEditor img')
                    # for i in range(0, len(item_pic)):
                    #     if (item_pic[i]):
                    #         img = item_pic[i]['src']
                    #         print(img)
                    #         save.write(img)
                    #         save.write('\n')
                    #     else:
                    #         break

                else:
                    print(response.status_code)
            except:
                exception = open('./exception.txt', 'w')
                exception.write(item_name)
                exception.write('\n')
