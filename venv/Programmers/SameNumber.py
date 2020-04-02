def solution(arr):
    answer=[]
    for c in range(len(arr)-1):
        if arr[c] != arr[c+1]:
            answer.append(arr[c])
    answer.append(arr[len(arr)-1])
    return answer

