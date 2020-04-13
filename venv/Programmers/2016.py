
def solution(a, b):
    arr = ["FRI", "SAT","SUN", "MON", "TUE", "WED", "THU"]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num =0
    if a != 1:
        for i in range(a-1):
            num+=day[i]
        num = num+b
        print(num)
        return arr[num%7-1]
    return arr[b%7-1]

print(solution(6,30))

