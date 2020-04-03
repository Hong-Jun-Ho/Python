def solution(n, m):
    answer = [n, m]
    answer.sort()

    ## 최대 공약수 구하기
    X = answer[0]
    Y = answer[1]
    while True:
        R = Y % X
        if(R==0):
            break
        else:
            Y = X
            X = R

    ## 최소 공배수 구하기
    X2= n*m/X

    return [X,X2]