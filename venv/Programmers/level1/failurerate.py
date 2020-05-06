## 실패율 ( 카카오 코딩테스트)
## 전체 스테이지의 개수 N, 현재 멈춰있는 스테이지의 번호가 담긴 stages가 매개변수로 주어짐
## 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 리턴
## 배열 내에 원소의 누적 개수를 파악해야함

def solution(N, stages):
    length = len(stages)
    result = []
    for i in range(1, N + 1):
        Pass = stages.count(i)
        if Pass == 0:
            failure = 0
        else:
            failure = Pass/length
        result.append((failure,i))
        length -= Pass

    result.sort(key=lambda x: x[0], reverse=True)
    return [i[1] for i in result]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
