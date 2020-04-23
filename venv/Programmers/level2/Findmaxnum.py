## Level2 가장 큰 수 찾기
def solution(numbers):
    numbers = list(map(str,numbers))
    New_list=[]
    for i in range(len(numbers)):
        if len(numbers[i]) == 4:
            New_list.append(str(numbers[i])*3+"4")
        if len(numbers[i]) == 3:
            New_list.append(str(numbers[i])*4+"3")
        if len(numbers[i]) == 2:
            New_list.append(str(numbers[i])*6+"2")
        if len(numbers[i]) == 1:
            New_list.append(str(numbers[i])*12+"1")

    New_list.sort(reverse=True)
    print(New_list)
    result=[]
    for e in range(len(New_list)):
        result.append(New_list[e][0:int(New_list[e][-1])])

    answer = "".join(result)
    print(answer)
    return answer

    ## 정답확인
print(solution([3, 321, 342, 33, 1]))
