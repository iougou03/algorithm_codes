import sys
from collections import deque

direction = ((1,0), (0,1), (-1,0), (0,-1))
N, M = map(int, sys.stdin.readline().split())
mapList = []

for _ in range(N):
    mapList.append(list(map(int, list(sys.stdin.readline()[:-1]))))

def bfs():
    global N, M
    queue = deque([[0, 0, 1]])
    visitied = [[[0,0] for _ in range(M)] for __ in range(N)]
    
    while queue:
        cx, cy, wall = queue.popleft()

        if cx == M - 1 and cy == N - 1:
            return visitied[cy][cx][wall] + 1

        for dx, dy in direction:
            nx = dx + cx ; ny = dy + cy
            if 0 <= nx < M and 0 <= ny < N:
                if mapList[ny][nx] == 1 and wall:
                    visitied[ny][nx][0] = visitied[cy][cx][wall] + 1
                    queue.append([nx, ny, 0])
                    
                elif mapList[ny][nx] == 0 and visitied[ny][nx][wall] == 0:
                    visitied[ny][nx][wall] = visitied[cy][cx][wall] + 1
                    queue.append([nx, ny, wall])

    return -1

mapList[0][0] -= 1
print(bfs())

# [print(m) for m in mapList]
