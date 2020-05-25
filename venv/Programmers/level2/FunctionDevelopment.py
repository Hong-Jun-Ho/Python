def solution(progresses, speeds):
    answer = []
    count = 0
    n = 0
    while True:
        if progresses[n] >= 100:
            if n == len(progresses) - 1:
                count += 1
                answer.append(count)
                break
            n += 1
            count += 1
        else:
            for j in range(len(progresses)):
                progresses[j] += speeds[j]
            if count != 0:
                answer.append(count)
                count = 0

    return answer


print(solution([96, 30, 55], [1, 30, 5]))
