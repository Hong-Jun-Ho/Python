
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

def solution(n):
    count =0
    for e in range(n+1):
        if is_prime_not_bad(e) == True:
            count += 1
    return count


print(solution(10)) 
