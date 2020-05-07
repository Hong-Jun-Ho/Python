## 위장
## 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장한다
## 2차원 배열이 주어짐
## 서로 다른 옷의 조합의 수를 return
## 스파이는 하루에 최소 한 개의 의상은 입는다.

## 1. 단순히 생각해보자
## 2. 하나씩 다 걸칠 경우 = 모자의 수 * 안경의 수 * 위장의 수
## 3. 그러면 모자를 쓰지 않을 경우, 안경을 쓰지 않을 경우, 위장을 하지 않을 경우가 포함이 안됨 +1 씩 해주면 경우의 수 끝
## 4. 최소 한 개의 의상은 입으니 모두다 안입는 경우의 수를 빼주면 된다.  -1
## 그러면 ! (모자의 수 +1) * (안경의 수 +1) * (위장의수 +1) -1 이다.
## 예시로 검증 1번 예시 =>  모자 2  안경 1   =>  (2+1) * (1+1) - 1 = 5
## 2번예시 위장3 => (3+1) - 1 = 3
## 어떠한 알고리즘을 쓸까??
## 2중 for문은 너무 시간복잡도와 공간복잡도가 난잡해짐
## for I in range(list)
##      for e in range list
##          if list[i][1] == list[e][1]:
##              count ++
## 위와 같은 방법을 쓰면 답은 나오겠지만... pass

def solution(clothes):
    answer = 1
    clotheslist = []
    for x, y in clothes:
        clotheslist.append(y)

    key = set(clotheslist)
    key = list(key)

    for e in range(len(key)):
        answer = answer * (clotheslist.count(key[e]) + 1)
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
