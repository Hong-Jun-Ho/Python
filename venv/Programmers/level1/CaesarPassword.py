def solution(s, n):
    answer = ''
    pluslist = []
    for e in s:
        if ord(e) == 32:
            pluslist.append(32)
        if 64 < ord(e) < 91:
            if 90 < (ord(e) + n):
                pluslist.append(ord(e) + n - 26)
            else:
                pluslist.append(ord(e) + n)
        elif 96 < ord(e) < 123:
            if (ord(e) + n) > 122:
                pluslist.append(ord(e) + n - 26)
            else:
                pluslist.append(ord(e) + n)

    result = list(map(chr, pluslist))
    answer = ''.join(result)

    return answer


print(solution("a B z", 4))
