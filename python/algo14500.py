import sys

direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
direction2 = (
    [(1, 0), (0, 1), (-1, 0)],
    [(0, 1), (0, -1), (-1, 0)],
    [(0, 1), (0, -1), (1, 0)],
    [(1, 0), (-1, 0), (0, -1)],
    )
input = sys.stdin.readline

mapArr = []
n, m = map(int, input().split())

for _ in range(n):
    mapArr.append(list(map(int, input().split())))

ans = 0

def checkShape(x, y, level, val):
    global n, m, ans

    if level == 4:
        ans = max(ans, val)
        return

    for dx, dy in direction:
        nx = dx + x ; ny = dy + y

        idx = ny * m + nx

        if (0<=nx<m and 0<=ny<n) and not visited[idx]:
            visited[idx] = 1
            checkShape(nx, ny, level + 1, val + mapArr[ny][nx])
            visited[idx] = 0

def checkShape2(x, y, level, val):
    global n, m, ans

    if level == 4: return

    state = True
    valCopy = val
    for dx, dy in direction2[level]:
        nx = dx + x ; ny = dy + y

        if 0<=nx<m and 0<=ny<n: 
            valCopy += mapArr[ny][nx]
        else: 
            state = False
            break
    if state: ans = max(ans, valCopy)

    checkShape2(x, y, level + 1, val)

def solution2(x, y):
    global n, m

    if 0<=x<m and 0<=y<n:
        if visited2[y * m + x]: return

        visited2[y * m + x] = 1
        checkShape2(x, y, 0, mapArr[y][x])
        
        solution2(x + 1, y)
        solution2(x, y + 1)

visited = [0 for _ in range(n * m)]
for y in range(n):
    for x in range(m):
        visited[y * m + x] = 1
        checkShape(x, y, 1, mapArr[y][x])
        visited[y * m + x] = 0

visited2 = [0 for _ in range(n * m)]
solution2(0, 0)

print(ans)