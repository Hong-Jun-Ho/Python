def solution(n, arr1, arr2):
    answer = []
    result = []
    for e in range(n):
        a = bin(arr1[e] | arr2[e]) + "n"
        result.append(a[-n - 1:-1])

    table = str.maketrans('b10', ' # ')
    for i in range(len(result)):
        answer.append(result[i].translate(table))

    return answer

print(solution(6,[46, 33, 33, 22, 31, 50],[27, 56, 19, 14, 14, 10]))