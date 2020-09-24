import copy
import collections
from sys import stdin
input = stdin.readline

N,M,answer,num_clean = 0
lab = [[0 for _ in range(8)] for _ in range(8)]
q_virus_original = collections.deque()

def check_new_position(r, c, arr):
    return False if (r >=N or c>=M or arr[r][c]) else True

def do_virus():
    global answer
    q_virus = copy.deepcopy(q_virus_original)
    lab_after_virus = copy.deepcopy(lab)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    num_virus = 0
    while q_virus:
        r, c = q_virus.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not check_new_position(nr, nc, lab_after_virus):
                continue
            lab_after_virus[nr][nc] = 2
            num_virus += 1
            q_virus.append((nr, nc))
    answer = max(answer, num_clean - num_virus - 3)

def build_wall(index, num_walls):
    for cur in range(index, N*M):
        if lab[cur//M][cur%M] != 0:
            continue
        lab[cur // M][cur % M] = 1
        do_virus() if num_walls==2 else build_wall(cur+1, num_walls + 1)
        lab[cur//M][cur%M] = 0
        if num_walls ==2 : return

N, M = map(int, input().split())
for r in range(N):
    l = list(map(int, input().split()))
    for c in range(M):
        lab[r][c] = l[c]
        num_clean+=1 if l[c]==0 else q_virus_original.append((r, c))

build_wall(0, 0)
print(answer)