# def solution(skill, skill_trees):
#     answer = 0
#
#     for skill_element in skill_trees:
#         index = 0
#         count = 0
#         for order in skill:
#             try:
#                 if index > skill_element.index(order):
#                     break
#                 else:
#                     index = skill_element.index(order)
#                     count += 1
#             except ValueError:
#                 if order == skill[0]:
#                     break
#                 if not skill_element[index - 1]:
#                     break
#                 else:
#                     count += 1
#                 index = len(skill_element)
#
#             if len(skill) == count:
#                 answer += 1
#
#     return answer
#
#
# print(solution("ABCD",  ["ABCGEGEGWEGED"]))
#

def solution(skill, skill_trees):
    answer = 0

    for skill_element in skill_trees:
        list = []
        Test = True

        for i in skill_element:
            if i in skill:
                list.append(i)

        for j in range(len(list)):
            if list[j] != skill[j]:
                Test = False
                break
        if Test == True:
            answer += 1
    return answer


print(solution("ABCD", ["ABCGEGEGWEGED"]))
