# https://2.python-requests.org/en/master/user/advanced/#id1
# pip install requests

import requests
import time


def fetcher(session, url):
    # context manager 키워드
    # 세션: 서버와 클라이언트 사이에서 연결을 계속 유지시켜주는 상태
    with session.get(url, verify=False) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    # session = requests.Session()
    # session.get(url)
    # session.close()
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 12
