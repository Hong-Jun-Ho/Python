def solution(brown, yellow):
    area = brown + yellow
    answer = []
    for x in range(brown):

        try:
            if x == (brown + 4 - (2 * area) / x) / 2:
                answer.append(x)
        except ZeroDivisionError:
            print("error")

    answer.sort(reverse=True)
    if len(answer)==1:
        answer.append(answer[0])
    return answer