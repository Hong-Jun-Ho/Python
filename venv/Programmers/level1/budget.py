def solution(d, budget):
    answer = 0
    d.sort()
    for e in range(len(d)):
        budget = budget - d[e]
        if budget < 0:
            answer = e
            return answer
    answer = len(d)
    return answer


print(solution([1, 3, 2, 5, 4], 9))
