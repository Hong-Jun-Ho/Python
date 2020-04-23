def solution(a, b):
    if a==b :
        return a
    arr=[a,b]
    arr.sort()
    answer = 0
    for e in range(arr[0],arr[1]+1):
        answer+=e

    return answer