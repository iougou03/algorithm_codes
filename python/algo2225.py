M = 1000000000

n, k = map(int , input().split())

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(n + 1): 
    dp[1][i] = 1

for i in range(n + 1):
    for j in range(2, k + 1):
        for m in range(i + 1):
            dp[j][i] += dp[j - 1][m]
            dp[j][i] %= M

print(dp[k][n])