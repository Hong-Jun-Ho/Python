def solution(w, h):
    def gcd(a, b):
        gcd = 1
        for k in range(2, min(a, b) + 1):
            while (a % k == 0) and (b % k == 0):
                a = a // k
                b = b // k
                gcd = gcd * k
                continue
        return gcd

    answer = w * h - (w + h - gcd(w,h))

    return answer


print(solution(8, 12))
