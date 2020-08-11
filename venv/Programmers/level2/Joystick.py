def solution(name):
    answer = 0
    temp = list(name)
    i = 0
    base = ["A"]*len(name)
    while True:
        right = 1
        left = 1
        if temp[i] != "A":
            if abs(ord(temp[i]) - 65) <= abs(91 - ord(temp[i])):
                answer += abs(ord(temp[i]) - 65)
            else:
                answer += abs(91 - ord(temp[i]))
            temp[i]="A"
        if temp == base:
            break
        else:
            for j in range(1, len(temp)):
                if temp[i + j] == "A":
                    right += 1
                else:
                    break
                if temp[i - j] == "A":
                    left += 1
                else:
                    break
            if right > left:
                answer += left
                i-=left
            else:
                answer += right
                i+=right

    return answer


print(solution("AAABA"))
