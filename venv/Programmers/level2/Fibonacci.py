def solution(n):
    Fibonacci = [0]*(n+1)
    Fibonacci[1] = 1

    if n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            Fibonacci[i] = (Fibonacci[i - 2] + Fibonacci[i - 1]) % 1234567
        return Fibonacci[i]


print(solution(8))
