import requests
import time
import os
import threading
import warnings

warnings.filterwarnings("ignore")


def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url, verify=False) as response:
        return response.text


def main():
    # urls = ["https://google.com"] * 50
    urls = ["https://google.com", "https://apple.com"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        # print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 23
