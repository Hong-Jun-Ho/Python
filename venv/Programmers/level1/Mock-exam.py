from itertools import cycle

def solution(answers):
    winner = []
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_supo = [0, 0, 0]

    ## zip은 제일 짧은 값을 기준으로 정렬해준다.
    zipped = list(zip(cycle(pattern_1), cycle(pattern_2),cycle(pattern_3),answers))

    print(zipped)

    for e in range(len(zipped)):
        if zipped[e][0] == zipped[e][3]: score_supo[0] += 1
        if zipped[e][1] == zipped[e][3]: score_supo[1] += 1
        if zipped[e][2] == zipped[e][3]: score_supo[2] += 1

    print(score_supo)

    if score_supo[0] >= score_supo[1] and score_supo[0] >= score_supo[2] : winner.append(1)
    if score_supo[1] >= score_supo[0] and score_supo[1] >= score_supo[2] : winner.append(2)
    if score_supo[2] >= score_supo[0] and score_supo[2] >= score_supo[1] : winner.append(3)



    return winner 

print(solution([1,2,3,4,5]))
