import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():

    result = await asyncio.gather(
        delivery("A", 1),
        delivery("B", 2),
        delivery("C", 3),
    )

    print(result)


# # 동시성 프로그래밍을 하지 않고,
# # 비동기 함수에서 동기 코드와 같음
# async def main():
#     await delivery("A", 1)
#     await delivery("B", 2)
#     await delivery("C", 3)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
