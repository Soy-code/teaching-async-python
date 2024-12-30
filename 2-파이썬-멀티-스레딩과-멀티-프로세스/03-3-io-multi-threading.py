# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    # params: (<requests.sessions.Session object at 0x000002C1291DBF10>, 'https://google.com')
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    # 멀티스레드..? max_workers=1이면 싱글스레드
    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        # 실행시키고 싶은 fetcher함수와, parameter를 적어줌
        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 6.8
