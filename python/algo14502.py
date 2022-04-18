from collections import deque

n, m = map(int, input().split())
matrix = []
virusList = []
safeCnt = 0
ans = float("inf")

for y in range(n):
    matrix.append(list(map(int, input().split())))
    for x in range(m):
        if matrix[y][x] == 0: safeCnt += 1
        elif matrix[y][x] == 2: virusList.append((x, y))

def matrixC3_recursive(level):
    if level == 3:
        bfs()
        return 
    
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 0:
                matrix[y][x] = 1
                matrixC3_recursive(level + 1)
                matrix[y][x] = 0

def bfs():
    global n, m, ans
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

    visited = [0 for _ in range(n * m)]
    queue = deque(virusList) ; virusCnt = 0

    while queue:
        cx , cy = queue.popleft()
        if visited[cy * m + cx]: continue
        visited[cy * m + cx] = 1 ; virusCnt += 1

        for dx, dy in directions:
            nx = dx + cx ; ny = dy + cy
            if 0<=nx<m and 0<=ny<n:
                if matrix[ny][nx] == 0 and not visited[ny * m + nx]:
                    queue.append((nx, ny))
    
    ans = min(ans , virusCnt - len(virusList))

matrixC3_recursive(0)
print(safeCnt - ans - 3)

# -----------------------------------------------------------
from collections import deque

n, m = map(int, input().split())
matrix = []
nonBlockedList = []
virusList = []
safeCnt = 0

for y in range(n):
    matrix.append(list(map(int, input().split())))
    for x in range(m):
        if matrix[y][x] == 0: 
            nonBlockedList.append((x, y))
            safeCnt += 1
        if matrix[y][x] == 2: virusList.append((x, y))

def matrixC3():
    l = len(nonBlockedList)
    ans = float("inf")

    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                blockedList = [
                    nonBlockedList[i],
                    nonBlockedList[j],
                    nonBlockedList[k],
                ]
                ans = min(ans, bfs(blockedList))

    return ans

def bfs(blockedList):
    global n, m    
    matrixCopy = [] ; directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
    for line in matrix:
        matrixCopy.append(line.copy())

    for bx, by in blockedList:
        matrixCopy[by][bx] = 1

    visited = [0 for _ in range(n * m)]
    queue = deque(virusList)
    virusCnt = 0

    while queue:
        cx , cy = queue.popleft()
        if visited[cy * m + cx]: continue
        visited[cy * m + cx] = 1

        for dx, dy in directions:
            nx = dx + cx ; ny = dy + cy
            if 0<=nx<m and 0<=ny<n:
                if matrixCopy[ny][nx] == 0:
                    matrixCopy[ny][nx] = 2 ; virusCnt += 1
                    queue.append((nx, ny))

    return virusCnt

print(safeCnt - 3 - matrixC3())