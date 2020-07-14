from itertools import permutations


def all_num():  # 123-987 각자 서로 다른 3자리의 임의의 숫자
    numbers = list(range(1, 10))
    all_number = list(permutations(numbers, 3))
    return all_number


def check_guess(guess, num):
    # baseball에 주어진 s,b수와 실제 s,b수 비교해서 같으면 T, 다르면 F 반환

    guess_num = [int(i) for i in str(guess[0])]
    guess_s = guess[1]
    guess_b = guess[2]
    strike, ball = 0, 0

    for i in range(3):
        if guess_num[i] == num[i]:
            strike += 1
            continue
        if guess_num[i] in num:
            ball += 1

    if guess_s == strike and guess_b == ball:
        return True
    else:
        return False


def solution(baseball):
    all_numbers = all_num()  # (1,2,3)~(9,8,7)
    answer = 0
    for num in all_numbers:
        Test = True
        for guess in baseball:
            if not check_guess(guess, num):
                Test = False
        if Test:  # baseball의 모든 케이스에서 True가 나왔을 경우 answer+1
            answer += 1

    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))