def solution(n,S):
    count = 0
    for i in range(n):
        count +=1
        for j in range(n):
            count+=1
            if S[j]<S[i]:
                temp= S[i]
                S[i]=S[j]
                S[j]=temp
                count+=1
    return count

print(solution(9,[12,5,46,3,1,3,67,8,436]))
