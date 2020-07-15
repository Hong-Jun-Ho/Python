def solution(citations):
    answer = 0
    citations.sort(reverse=True) # 정렬
    citations.append(0) ## index 값 넘어가는 걸 방지하기 위해 0 추가
    print(citations)

## 정렬 후 인용된 수, 인용된 논문 개수 를 check 하여 return
    for i in range(len(citations)):
        if citations[i] >= i+1 and citations[i+1] <= i+1:
            return i + 1
    return answer


print(solution([5, 5, 5, 5, 5]))
