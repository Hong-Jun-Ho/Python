def solution(n, lost, reserve):
    C_list = [1] * n
    for i in reserve:
        C_list[i - 1] = 2
    for i in lost:
        C_list[i - 1] = C_list[i - 1] - 1

    for index, value in enumerate(C_list):
        if index > 0 and value == 0 and C_list[index - 1] == 2:
            C_list[index] = 1
            C_list[index - 1] = 1
        elif index < n - 1 and value == 0 and C_list[index + 1] == 2:
            C_list[index] = 1
            C_list[index + 1] = 1

    return n - C_list.count(0)
