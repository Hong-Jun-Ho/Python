def solution(numbers, target):
    stack = [numbers[0]]
    for i in numbers[1:]:
        calculate = []
        for j in stack:
            calculate.append(j + i)
            calculate.append(j - i)
        stack = calculate
    return stack.count(target)+stack.count(-target)


print(solution([1, 1, 1, 1, 1], 3))

# n개의 음이 아닌 정수가 있다.
# 이 수를 적절히 더하거나 빼서 타겟넘버를 만들어야 함
# 각 숫자는 1이상 50이하인 자연수
# 주어지는 숫자의 개수는 2 이상, 20개 이하
# 타겟 넘버는 1이상 1000 이하
# 조합의 개수를 찾아야 한다.
# 우선 n개를 다써야함 #
#테스트 1 〉	통과 (88.78ms, 29.7MB)
#테스트 2 〉	통과 (87.48ms, 25.7MB)
#테스트 3 〉	통과 (0.12ms, 10.8MB)
#테스트 4 〉	통과 (0.37ms, 10.8MB)
#테스트 5 〉	통과 (2.66ms, 10.9MB)
#테스트 6 〉	통과 (0.21ms, 10.6MB)
#테스트 7 〉	통과 (0.12ms, 10.8MB)
#테스트 8 〉	통과 (0.75ms, 10.8MB)
#
#
#
#
#
