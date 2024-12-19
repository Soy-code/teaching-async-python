# https://docs.aiohttp.org/en/stable/
# pip install aiohttp~=3.7.3

import aiohttp
import time
import asyncio


# fetcher 자체를 코루틴으로 만듦
async def fetcher(session, url):
    # async 키워드를 해당하는 context 에서도 붙어야 함
    async with session.get(
        # SSL Error 발생하여 추가
        url,
        headers=session.headers,
    ) as response:
        # response.text 자체가 awaitable임
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        # result = await fetcher(session, urls[0])
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    # 코루틴을 실행하기 위한 asyncio 메소드 사용
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 12초 -> 5.4초 줄어듦
