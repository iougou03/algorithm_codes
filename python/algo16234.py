import sys
from collections import deque

input = sys.stdin.readline
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
N, L, R = map(int, input().split())

countires = []

for i in range(N):
    countires.append(list(map(int, input().split())))

def bfsOpenGates(
    startx:int, 
    starty:int, 
    n:int, 
    left:int, 
    right:int,
    ):
    global countires, visited

    queue = deque([[startx, starty]])
    cnt = 0 ; popular = 0
    visitList = []

    while queue:
        cx, cy = queue.popleft()

        if visited[cx + cy * n]: continue
        visited[cx + cy * n] = 1
        cnt += 1 ; popular += countires[cy][cx]
        visitList.append(cy * n + cx)

        for dx , dy in direction:
            nx = dx + cx ; ny = dy + cy
            if (0 <= nx < n and 0 <= ny < n) and not visited[ny * n + nx]:
                v = abs(countires[cy][cx] - countires[ny][nx])

                if left <= v <= right:
                    queue.append([nx, ny])

    val = popular // cnt
    
    for idx in visitList:
        countires[idx // n][idx % n] = val

    if cnt <= 1: return [False, []]
    
    return [True, visitList]

changed = True
days = 0
cand = [(y * N + x) for y in range(N) for x in range(y % 2,N,2)]

while changed:
    changed = False
    visited = [0 for _ in range(N * N)]
    c = []

    for idx in cand:
        if not visited[idx]:
            state, changedCountries = bfsOpenGates(idx % N, idx // N, N, L, R)
            c.extend(changedCountries)
            if state: changed = True

    if changed:
        cand = c
        days += 1
    else: break

print(days)
