
# 구명보트 최대 인원수 : 2명
# 구명보트를 최대한 적게 사용
# 모든 사람을 구출하기 위한 구명보트의 최솟값 return

def solution(people, limit):
    answer = 0
    people.sort()
    import collections
    deq = collections.deque(people)

    print(deq)
    while deq:
        sum_kg = deq[0] + deq[-1]
        if len(deq) == 1 :
            answer+=1
            break
        if sum_kg>limit:
            deq.pop()
            answer += 1
        if sum_kg<=limit:
            deq.pop()
            deq.popleft()
            answer += 1

    return answer

print(solution([70, 80, 50],100))