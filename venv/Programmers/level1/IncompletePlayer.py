## 프로그래머스 level_1 완주하지 못한 선수
def solution(participant, completion):
    ## set함수를 사용하여 받은 배열을 중복을 제거하고 원소단위로 setting해준다.
    participant_set = set(participant)
    completion_set = set(completion)
    print (participant_set)
    print (completion_set)
    result = list(participant_set - completion_set)
    print(result)

    ## 동명 2인이 있다면 result값이 비어있을 수 있다. 그러한 경우 else로 count하여 동명 2인을 찾아낸다.
    if result !=[]:
        return result[0]
    else:
        for c in completion:
            a=completion.count(c)
            print(a)
            b=participant.count(c)
            print(b)
            if(a != b):
                return c
    return None 

print(solution(["eand", "kiki", "kiki"],["eand", "kiki"]))
