def solution(N, M):
    answer = []
    scores = []
    x = 0
    for i in range(len(N)):
        x += N[i]
        scores.append(x)

    print(scores)

    for [x, y] in M:
        if x == 1:
            answer.append(scores[y - 1])
        else:
            answer.append(scores[y - 1] - scores[x - 2])

    return answer


print(solution([10, 20, 30, 40, 50], [[1, 3], [2, 3], [3, 5]]))
