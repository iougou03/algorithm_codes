direction = ((1, 0), (0, 1), (1, 1))

n, m = map(int, input().split())
candies = []
for _ in range(n):
    candies.append(list(map(int , input().split())))
    
dp = [[0] * (m + 1) for _ in range(n + 1)]

for y in range(1, n + 1):
    for x in range(1, m + 1):
        v = 0
        for dx, dy in direction:
            v = max(v, dp[y - dy][x - dx])
        
        dp[y][x] = v + candies[y - 1][x - 1]

print(dp[n][m])