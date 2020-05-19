# 다트 게임은 총 3번의 기회로 구성된다
# 점수는 0~10점
# 점수와 함께, S, D, T 1제곱, 2제곱, 3제곱
# 옵션이 있다. *: 해당점수와 이전 점수 2배 #: -해당점수
# *은 첫번째 기회에서 나올 수 있다. 이경우 첫번째만 2배
# *은 다른 *과 중첩될 수 있다. 4배
# *의 효과는 #과도 중첩될 수 있다. 이 경우 중첩된 #의 점수는 -2배
# S,D,T는 점수마다 하나씩 존재
# *,#은 둘 중 하나만 존재가능, 존재하지 않을 수도 있다.

# 점수 + SDT + ('' or * or #)
# 점수 + 3가지 경우의수 + 3가지 경우의 수
# 점수가 아니면, 앞의 점수 값에 * -1 혹은 *2 혹은 **2 혹은 **3 을 해주면 됨
# 정확성 Test만 있다. 시간복잡도 필요 없음


def solution(dartResult):
    point = []
    temp = ''
    for i in dartResult:
        if 47 < ord(i) < 58:
            temp += i
        elif i == 'S':
            point.append(int(temp))
            temp = ''
        elif i == 'D':
            point.append(int(temp) ** 2)
            temp = ''
        elif i == 'T':
            point.append(int(temp) ** 3)
            temp = ''
        elif i == '*':
            if len(point) > 1:
                point[-2] *= 2
            point[-1] *= 2
        elif i == '#':
            point[-1] *= -1
    return sum(point)


print(solution("1D#2S*3S"))
# 1^2 * (-1) * 2 + 2^1 * 2 + 3^1
