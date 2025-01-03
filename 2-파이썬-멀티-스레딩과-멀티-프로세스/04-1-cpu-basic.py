import os
import sys
import time
import threading

# # ValueError 발생 시
# sys.set_int_max_str_digits(1000000)

# nums = [50, 63, 32]
nums = [30] * 100


# 단순한 연산 코드
def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    results = [cpu_bound_func(num) for num in nums]
    # print(results)
    # results 값이 너무 커서 ValueError 발생
    print(len(results))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 49.37, 34
    # 13초
