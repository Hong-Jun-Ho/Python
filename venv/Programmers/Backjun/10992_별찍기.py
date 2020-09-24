# n = int(input())
#
# for i in range(n - 1):
#     for j in range(n * 2 - 1):
#
#         if j == n - i - 1:
#             print('*', end='')
#         elif j == n + i - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#
# print('*' * (n * 2 - 1))
# 출력 형식이 잘못됨

n = int(input())

for i in range(1, n + 1):
    if i == n:
        print('*' * (2 * i - 1))
    elif i == 1:
        print(' ' * (n - i)+ '*')
    else:
        print(' ' * (n - i)+ '*'+ ' ' * (2 * i - 3)+ '*')
