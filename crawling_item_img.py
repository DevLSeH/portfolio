import urllib.request
import requests
import time
import os
import re

root_dir = '남성향수'
for (root, directories, files) in os.walk('./상품/{}'.format(root_dir)):
    base_path = './상품이미지/{}'.format(root_dir)
    direct = os.makedirs(base_path)

    for file in files:
        file_path = os.path.join(root, file)
        f = open(file_path, 'r', encoding='UTF-8')

        item_name = ''
        count_line = 1
        count = 1
        for url in f:
            if (count_line == 1):
                count_line += 1

            elif (count_line == 2):
                item_name = url.replace('/', '').replace(
                    '\\', '').replace('\t', '').replace('\n', '').replace('*', '').replace(
                    '#', '').replace(' ', '_').replace('/', '').replace(
                    '.', '').replace('[', '').replace(']', '')
                print(item_name)
                count_line += 1

            elif (count_line == 3):
                count_line += 1

            elif (url.startswith('https')):
                if (url.endswith('.gif')):
                    continue

                else:
                    path = base_path + '/' + item_name
                    item_path = path + '/' + \
                        '{0}_{1}.jpg'.format(item_name, count)

                    if (count == 1):
                        dir = os.makedirs(path)
                    # urllib 사용 방식 (한글 url 문제 발생)
                    # url = urllib.parse.quote(url)
                    # urllib.request.urlretrieve(
                    #     url, path )
                    pic = requests.get(url)
                    with open(item_path, 'w+b') as save:
                        save.write(pic.content)
                    count += 1

            else:
                continue
