def solution(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    if count == 0:
        return True
    else:
        return False

### 괄호가 바르게 짝지어졌다는 것은
## '(' 문자로 열렸으면 반드시 짝지어서 ')'로 닫혀야 한다는 듰
## 문제 풀이 s는 (or )로만 이루어져 있음

## ( 을 만났다 그다음 )를 찾는다
##
