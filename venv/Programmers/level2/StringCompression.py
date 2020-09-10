def solution(s):
    answer = s
    LenS = len(s)
    if len(s) == 1 or len(s) == 2 or len(s) == 3:
        return len(s)

    for unit in range(1, len(s) // 2+1):
        temp_a = ""
        temp = s[:unit]
        cnt = 1
        for i in range(unit, len(s), unit):
            if temp == s[i:i + unit]:
                cnt += 1
            else:
                if cnt == 1:
                    temp_a += temp
                else:
                    temp_a += str(cnt) + temp
                cnt = 1
                temp = s[i:i + unit]

        if cnt == 1:
            temp_a += temp
        else:
            temp_a += str(cnt) + temp

        if len(temp_a) < LenS:
            answer = temp_a
            LenS = len(answer)

    return len(answer)


print(solution("aabbaccc"))
