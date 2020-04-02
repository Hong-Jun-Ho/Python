
def solution(participant, completion):
    participant_set = set(participant)
    completion_set = set(completion)
    print (participant_set)
    print (completion_set)
    result = list(participant_set - completion_set)
    print(result)
    if result !=[]:
        return result[0]
    else:
        for c in completion:
            a=completion.count(c)
            b=participant.count(c)
            if(a != b):
                return c
    return None

print(solution(["kiki", "kiki", "kiki"],["kiki", "kiki"]))
