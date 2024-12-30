import time
import os
import sys
import threading
from concurrent.futures import ProcessPoolExecutor

# sys.set_int_max_str_digits(1000000)

nums = [30] * 100


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    # 멀티 프로세스 사용
    # 각각 다른 프로세스에서 함수를 맡음. 병렬로 실행하고 있음
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(len(results))
    # print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 22
    # 6초
