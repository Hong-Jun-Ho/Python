## 프로그래머스 level_1 같은 숫자는 싫어
def solution(arr):
    answer=[]
    ## n-1개 까지 다음숫자와 검증하고 중복되지 않으면 append 해줌
    for c in range(len(arr)-1):
        if arr[c] != arr[c+1]:
            answer.append(arr[c])

    ## 마지막 값은 for문에서 들어가지 않고 중복일 수 없으니 append해줌
    answer.append(arr[len(arr)-1])
    return answer


print(solution([1,1,3,3,0,1,1]))

