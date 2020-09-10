import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())

    result = 0

    for i in range(n):
        data = list(map(int,sys.stdin.readline().split()))
        min_value = 10001 # 입력조건보다 1큰 수 대입
        for j in data:
            min_value = min(min_value,j) # 가장 작은 값 찾기
        result = max(result,min_value) # 가장 작은 값 중에서 큰 값 찾기
    return result

print(solution())