# import copy
# import collections
# from sys import stdin
#
# input = stdin.readline
#
# N = 0
# M = 0
# lab = [[0 for _ in range(8)] for _ in range(8)]
# mirror = [[0 for _ in range(8)] for _ in range(8)]
# q_virus_original = collections.deque()
# answer = 0
# num_clean = 0
#
#
# def init_mirror():
#     global mirror
#     for r in range(N):
#         for c in range(M):
#             mirror[r][c] = lab[r][c]
#
#
# def check_new_position(r, c, arr):
#     if r < 0 or r >= N or c < 0 or c >= M:
#         return False
#     if arr[r][c] is not 0:
#         return False
#     return True
#
#
# def do_virus():
#     global answer
#     q_virus = copy.deepcopy(q_virus_original)
#     lab_after_virus = copy.deepcopy(mirror)
#     dr = [1, -1, 0, 0]
#     dc = [0, 0, 1, -1]
#     num_virus = 0
#     while q_virus:
#         r, c = q_virus.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if not check_new_position(nr, nc, lab_after_virus):
#                 continue
#             lab_after_virus[nr][nc] = 2
#             num_virus += 1
#             q_virus.append((nr, nc))
#     num_safe = num_clean - num_virus - 3
#     print(answer)
#     answer = max(answer, num_safe)
#
#
# def build_wall(row, col, num_walls):
#     if num_walls is 3:
#         do_virus()
#         return
#     col_begin = col
#     for r in range(row, N):
#         if r is not row:
#             col_begin = 0
#         for c in range(col_begin, M):
#             if mirror[r][c] is not 0:
#                 continue
#             mirror[r][c] = 1
#             build_wall(r, c, num_walls + 1)
#             mirror[r][c] = 0
#
#
# def solve():
#     for r in range(N):
#         for c in range(M):
#             if lab[r][c] is not 0:
#                 continue
#             init_mirror()
#             mirror[r][c] = 1
#             build_wall(r, c, 1)
#             mirror[r][c] = 0
#     print(answer)
#
#
# N, M = map(int, input().split())
# for r in range(N):
#     l = list(map(int, input().split()))
#
#     for c in range(M):
#         lab[r][c] = l[c]
#         if lab[r][c] is 0:
#             num_clean += 1
#         elif lab[r][c] is 2:
#             q_virus_original.append((r, c))
#
# solve()
#### 위에꺼는 예제는 정답은 나오지만 컴파일에러... 왜?? ##

## 아래는 DFS로 푼 정답 ##

# -*- coding: utf-8 -*-

import copy
import sys

n = m = 0
arr = []
virusList = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0


## 안전구역 넓이 구하기
def getSafeArea(copyed):
    safe = 0
    for i in range(n):
        for j in range(m):
            if copyed[i][j] == 0:
                safe += 1
    return safe


## DFS로 바이러스 퍼트리기
def spraedVirus(x, y, copyed):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if copyed[nx][ny] == 0:
                copyed[nx][ny] = 2
                spraedVirus(nx, ny, copyed)


## 조합으로 벽 3개 놓는 모든 경우 구하기
def setWall(start, depth):
    global maxVal

    if depth == 3:
        # 복사
        copyed = copy.deepcopy(arr)

        length = len(virusList)
        for i in range(length):
            [virusX, virusY] = virusList[i]
            spraedVirus(virusX, virusY, copyed)

        maxVal = max(maxVal, getSafeArea(copyed))
        return

    for i in range(start, n * m):
        x = (int)(i / m)
        y = (int)(i % m)

        if arr[x][y] == 0:
            arr[x][y] = 1
            setWall(i + 1, depth + 1)
            arr[x][y] = 0


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                virusList.append([i, j])

    ## 벽세우기
    setWall(0, 0)
    print(maxVal)