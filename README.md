# web-crawling
화장품 웹사이트에서 상품 정보를 크롤링하는 프로젝트
예시 코드는 올리브영 html 구조를 참고함

실행 순서
1. crawling_item_url.py
(주어진 url에서 상품 또는 개체에 입력된 src를 .txt로 저장)

2. crawling_item_body.py
(.txt에 저장된 링크 안에서 html parser를 통해 내부 정보를 크롤링, 이미지 링크를 .txt로 저장)

3. crawling_item_img.py
(.txt에 저장된 이미지 링크에서 이미지 파일을 다운로드)
