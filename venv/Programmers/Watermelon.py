def solution(n):
    a = "수박"
    b = a * (n // 2 + 1)
    answer = b[:n]

    return answer