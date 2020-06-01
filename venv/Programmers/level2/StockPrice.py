def solution(prices):
    answer = []
    for i in range(len(prices)):
        j = i + 1
        if i == len(prices)-1:
            answer.append(0)
            break
        while j <= len(prices)-1:
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
            else:
                j += 1
        else:
            answer.append(j-i-1)
    return answer


print(solution([1, 2, 2, 3, 3, 2, 2, 1, 1, 1]))
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
