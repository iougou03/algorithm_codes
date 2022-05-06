import sys
input = sys.stdin.readline
M = 1000000009

dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1][1] = 1

dp[2][2] = 1

dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] += dp[i - 1][2] % M + dp[i - 1][3] % M
    dp[i][2] += dp[i - 2][1] % M + dp[i - 2][3] % M
    if i - 3 >= 0:
        dp[i][3] += dp[i - 3][1] % M + dp[i - 3][2] % M

t = int(input())

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % M)
