def solution(w, h):
    def gcm(a, b):
        gcm = 1
        for k in range(2, min(a, b) + 1):
            while (a % k == 0) and (b % k == 0):
                a = a // k
                b = b // k
                gcm = gcm * k
                continue
        return gcm

    gcm = gcm(w, h)
    if gcm == 1:
        answer = w * h - (w + h - 1)
    else:
        answer = w * h - (w + h - gcm)

    return answer


print(solution(8, 12))
