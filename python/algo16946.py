import sys
from collections import deque

input = sys.stdin.readline
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

n, m = map(int, input().split())
matrix = []
matrixIsland = []
spaceCoor = []
islands = [0]

for y in range(n):
    matrix.append(list(map(int, list(input()[:-1]))))
    matrixIsland.append(matrix[y].copy())

    for x in range(m):
        if matrix[y][x] == 0:
            spaceCoor.append([x, y])

visited = [0 for _ in range(n * m)]

def bfsIsland(isladnIdx, startx, starty, n, m):
    queue = deque([[startx, starty]])
    maxCnt = 0

    while queue:
        x, y = queue.popleft()

        if visited[y * m + x]: continue
        visited[y * m + x] = 1
        maxCnt += 1 ; matrixIsland[y][x] = isladnIdx
        
        for dx, dy in direction:
            nx = x + dx ; ny = y + dy

            if (0<=nx<m and 0<=ny<n) and not visited[ny * m + nx]:
                if matrix[ny][nx] == 0: queue.append([nx, ny])

    return maxCnt

idx = -1
for x, y in spaceCoor:
    if not visited[y * m + x]:
        cnt = bfsIsland(idx, x, y, n, m)
        islands.append(cnt)
        idx -= 1

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1:
            islandVisited = []
            for dx, dy in direction:
                nx = x + dx ; ny = y + dy

                if (0<=nx<m and 0<=ny<n) and matrixIsland[ny][nx] < 0:
                    iidx = -matrixIsland[ny][nx]
                    if iidx not in islandVisited:
                        matrix[y][x] += islands[iidx]
                        islandVisited.append(iidx)
            matrix[y][x] %= 10

# for y in range(n):
#     for x in range(m):
#         print(matrixIsland[y][x],end=" ")
#     print()

for y in range(n):
    for x in range(m):
        print(matrix[y][x],end="")
    print()