def solution(s):
    q = []
    for c in range(len(s)):
        q.append(ord(s[c]))
    q.sort()
    q.reverse()

    for c in range(len(q)):
        q[c] =(chr(q[c]))

    result = ''.join(q)
    return result

print(solution("Zbcdefg"))


## 다른사람의 풀이

## def solution(s):
##     return ''.join(sorted(s, reverse=True)) 
