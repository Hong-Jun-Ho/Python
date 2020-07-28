# import itertools
#
#
# def solution(number, k):
#     answer = []
#     index = []
#     temp = ''
#     for i in range(len(number)):
#         index.append(i)
#     length = len(index) - 1
#     com = list(itertools.combinations(index, len(index) - k))
#     print(com)
#     for i in com:
#         for j in reversed(i):
#             temp += number[length - j]
#         answer.append(temp)
#         temp = ''
#
#     return str(max(answer))
#
#
# print(solution("4177252841", 4))

def solution(number, k):
    num_list = []

    for index, num in enumerate(number):
        if len(num_list) > 0:
            while k > 0 and num_list[-1] < num:
                num_list.pop()
                k -= 1
                if len(num_list) == 0:
                    break
        if k == 0:
            num_list += list(number[index:])
            break
        num_list.append(num)

    answer = ''.join(num_list)
    return answer


print(solution("4177252841", 4))
