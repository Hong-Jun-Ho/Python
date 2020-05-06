## X만큼 간격이 있는 n개의 숫자
## 문제 파악
## 정수 x와 자연수 n을 입력 받는다
## x부터 시작해 x씩 증가하는 숫자를 n 개 지니는 리스트 리턴
## 문제풀이
## for 문안에 x+=x 를 하면 끝
## x for happy
def solution(x, n):
    answer = []
    for e in range(n):
        x+=x
        answer.append(x)
    return answer

print(solution(-2,5))