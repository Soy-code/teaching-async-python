import requests


def io_bound_func():

    # 구글 서버에 요청을 보냄
    # SSL Error가 발생 ->  verify=False 추가
    result = requests.get("https://google.com", verify=False)
    return result


if __name__ == "__main__":
    for i in range(10):
        result = io_bound_func()
        print(result)
