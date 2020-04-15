## 소수 찾기
def is_prime_not_bad(n: int) -> bool:
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0:
            return False
    return True

## 프로그래머스 Level 2 소수 찾기
import itertools
import math
def solution(numbers):
    ## 받은 숫자를 배열로 잘라서 int화 시켜 넣는다.
    int_list = list(map(int,numbers))
    print("int list는 아래와 같습니다.")
    print(int_list)

    ## 1자리수 부터 ~ len(number)자리 까지 모든 경우의 수를 배열로 만든다
    cases=[]
    for e in range(len(int_list)):
        cases.append(list(itertools.permutations(int_list, len(int_list)-e))) ##int_list에서 몇개로 조합할지 결정

    joincases =[]
    for i in range(len(cases)):
        for j in range(len(cases[i])):
            temp=''.join(list(map(str,cases[i][j]))) ## 2차 배열에 있는 list를 스트링화 하여 join 후 전달함
            joincases.append(int(temp)) ## temp들 중 0으로 시작하는 값을 없애기 위해 정수형으로 변환 하여 1차배열로 만들어줌

    ## 중복제거
    result = set(joincases)
    ## 리스트화
    result = list(result)
    print(result)

    ## 소수 판별하기
    answer = []
    for e in range(len(result)):
        if is_prime_not_bad(result[e]):
            print("TRUE: %d은 소수 입니다. "%result[e])
            answer.append(result[e])
    print(answer)
    return len(answer)

## 정답 체크
print(solution("1712"))


## 소수를 찾는 알고리즘을 생각했었지만 자기자신과 나누어 질때까지 for문을 돌리니 오류가 났음
## 오래걸린 원인 : 시간효율성 생각 안함
## 깨달은점 : 함수를 하나 만들어서 return True, False를 이용하면 시간을 줄일 수 있음 알고리즘의 효율화와 직관성이 높아짐!!!! 기억하자