# C, R = map(int, input().split())
# K = int(input())
#
# def Search(x, y, finish):
#     if finish > x * y:
#         return print(0)
#     R = y
#     count = 1
#     row = y - 1
#     col = 0
#     y_range = y - 1
#     x_range = x - 1
#     while True:
#         ## 위로
#         for e in range(y_range):
#             row -= 1
#             count += 1
#             if count == finish:
#                 return print("%d %d" % (col + 1, R - row))
#         y_range -= 1
#         if row == 0:
#             y_range += 1
#
#         ## 오른쪽으로
#         for e in range(x_range):
#             col += 1
#             count += 1
#             if count == finish:
#                 return print("%d %d" % (col + 1, R - row))
#         x_range -= 1
#
#         ## 아래로
#         for e in range(y_range):
#             row += 1
#             count += 1
#             if count == finish:
#                 return print("%d %d" % (col + 1, R - row))
#         y_range -= 1
#
#         ## 왼쪽으로
#         for e in range(x_range):
#             col -= 1
#             count += 1
#             if count == finish:
#                 return print("%d %d" % (col + 1, R - row))
#         x_range -= 1
#
#
# Search(C, R, K)


def Within(lst, y, x, c, r):
    if x >= 0 and x < c and y >= 0 and y < r:
        if lst[y][x] == 0: return True
    return False

C, R = map(int, input().split())
person = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
idx = 0
x, y = 0, R-1
field = [[0 for i in range(C)] for j in range(R)]

for i in range(C*R):
    field[y][x] = i+1
    if person > C*R:
        print(0)
        break
    elif i+1 == person:
        print('{0} {1}'.format(x+1, R-y))
        break
    if not Within(field, y+dy[idx], x+dx[idx], C, R):
        idx = (idx + 1) % 4
    x += dx[idx]
    y += dy[idx]