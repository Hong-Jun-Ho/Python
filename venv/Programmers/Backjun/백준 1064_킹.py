a, b, c = input().split()
A = (ord(a[0]) - ord('A'), int(a[1]) - 1)
B = (ord(b[0]) - ord('A'), int(b[1]) - 1)

# 우측, 좌측, 하향, 상향 // 우상향 좌하향 우하향 좌하향
moves = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
         'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
for i in range(int(c)):
    move = moves[input()]
    NA = (A[0] + move[0], A[1] + move[1])
    if NA == B:
        NB = (B[0] + move[0], B[1] + move[1])
    else:
        NB = B
    if 0 <= NA[0] < 8 and 0 <= NA[1] < 8 and 0 <= NB[0] < 8 and 0 <= NB[1] < 8:
        A, B = NA, NB
print('%c%d' % (chr(ord('A') + A[0]), 1 + A[1]))
print('%c%d' % (chr(ord('A') + B[0]), 1 + B[1]))
