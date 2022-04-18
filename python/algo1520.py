import sys
sys.setrecursionlimit(250000)

input = sys.stdin.readline

m, n = map(int, input().split())
mapList = []
dp = [[-1 for _ in range(n)] for _ in range(m)]

for _ in range(m):
    mapList.append(list(map(int, input().split())))

def dfs(currentX, currentY):
    global m, n
    
    if dp[currentY][currentX] != -1:
        return dp[currentY][currentX]

    if currentX == n - 1 and currentY == m - 1:
        return 1
    
    dp[currentY][currentX] = 0

    direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
    
    for dx, dy in direction:
        nx = dx + currentX ; ny = dy + currentY
        if 0 <= nx < n and 0 <= ny < m:
            if mapList[currentY][currentX] > mapList[ny][nx]:
                dp[currentY][currentX] += dfs(nx, ny)

    return dp[currentY][currentX]

print(dfs(0, 0))