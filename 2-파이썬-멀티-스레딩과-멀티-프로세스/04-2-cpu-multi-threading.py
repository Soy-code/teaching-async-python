import time
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

# sys.set_int_max_str_digits(1000000)

nums = [30] * 100
# nums = [50, 63, 32]


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
    # Executor를 사용해서 multithreading
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(len(results))
    # print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 50, 36
    # 19초
    # 연산을 하는데 굳이 쓸데없이 동시성을 사용했기 때문에. 쓸데없이 비용만 올라간 것임
