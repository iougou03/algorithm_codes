import sys
input = sys.stdin.readline

n = int(input())
wines = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(n): wines[i + 1] = int(input())

dp[1] = wines[1]
if n > 1:
    dp[2] = wines[2] + wines[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], wines[i - 1] + dp[i - 3]) + wines[i]
        dp[i] = max(dp[i - 1], dp[i])

print(wines)
print(dp)
print(max(dp))