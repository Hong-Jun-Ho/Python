import sys


def solution():
    arr = []
    n, m, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    first = arr[n-1]
    second = arr[n-2]

    count = int(m/(k+1)) *k # 나누어 떨어질 때는 이 것으로 끝 배열의 반복
    count += m % (k+1)  # 나누어 떨어지지 않을 때를 고려해야함
    result = 0
    result += count *first ## 가장 큰 수가 더해지는 횟수
    result += (m-count) * second ## 두번 째 큰 수가 더해지는 횟수

    return result

print(solution())