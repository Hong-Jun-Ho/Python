def solution(s):
    answer = len(s)

    ## 문제에서 길이가 1~3 이면 나눌 필요가 없음
    if len(s) == 1 or len(s) == 2 or len(s) == 3:
        return len(s)

    ## 문자를 1~ 반까지 자르는 경우의 수
    for unit in range(1, len(s) // 2+1):
        temp_a = ""
        temp = s[:unit] ## 초기값 지정 문자열은 무조건 앞에서부터 정해진 길이만큼 잘라야함 == 문제 조건 중요!
        cnt = 1
        for i in range(unit, len(s), unit): #자른 길이만큼 구간별 확인
            if temp == s[i:i + unit]: # 자른 길이의 문자가 temp랑 같은지 확인
                cnt += 1
            else:
                if cnt == 1:
                    temp_a += temp
                else:
                    temp_a += str(cnt) + temp
                cnt = 1
                temp = s[i:i + unit] # 다음구간 확인을 위해 temp값 변경

        # 끝까지 확인한 후에 나머지 문자열을 붙여주기 위함
        if cnt == 1:
            temp_a += temp
        else:
            temp_a += str(cnt) + temp

        # 길이의 최소값 입력
        if len(temp_a) < answer:
            answer = len(temp_a)

    return answer


print(solution("abcabcdede"))
