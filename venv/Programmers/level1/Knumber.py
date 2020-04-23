## level1 - k번째 수 
def solution(array, commands):
    answer = []
    for e in range(len(commands)):
        i = commands[e][0] - 1
        j = commands[e][1]
        k = commands[e][2] - 1

        answer.append(sorted(array[i:j])[k])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
