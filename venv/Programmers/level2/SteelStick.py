def solution(arrangement):
    arrangement = arrangement.replace("()", 'L')
    print(arrangement)
    count = 0
    stick = 0
    for i in arrangement:
        if i == "(":
            stick += 1
        if i == "L":
            count += stick
        if i == ")":
            stick -= 1
            count += 1
    return count


print(solution("()(((()())(())()))(())"))
