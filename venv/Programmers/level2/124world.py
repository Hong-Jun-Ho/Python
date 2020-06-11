def solution(n):
    answer = ''
    world_diction = {1: "1", 2: "2", 0: "4"}
    QUOTIENT = 1
    MOD = 1

    while QUOTIENT != 0:
        QUOTIENT = n // 3
        MOD = n % 3
        if MOD == 0:
            QUOTIENT -= 1

        n = QUOTIENT
        answer = world_diction[MOD] + answer
    return answer

print(solution(12))
