import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


# async def main():

#     result = await asyncio.gather(
#         delivery("A", 1),
#         delivery("B", 2),
#         delivery("C", 3),
#     )

#     print(result)


async def main():
    # task는 예약을 해놓는 것
    task1 = asyncio.create_task(delivery("A", 2))
    task2 = asyncio.create_task(delivery("B", 1))

    # task로 미리 예약을 해놓고 await으로 아래와 같이 사용할 수 있음
    await task2
    await task1


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
