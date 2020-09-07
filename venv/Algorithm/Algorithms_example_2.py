def solution(n,S):
    result = 0
    count = 0
    for i in range(n):
        result +=S[i]
        count +=1
    return count

print(solution(3,[3,4,5,6,1,2]))