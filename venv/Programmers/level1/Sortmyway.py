import operator


def solution(strings, n):
    answer = []
    Dict = {}
    # ...1
    for i in strings:
        Dict[i] = i[n]

    sortedDict = sorted(Dict.items(), key=operator.itemgetter(1, 0))

    for i in sortedDict:
        answer.append(i[0])
    return answer
 

print(solution(["abce", "abcd", "cdx"], 2))
