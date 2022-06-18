n = int(input())

seq = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = seq[0]
dp[0][1] = 0
ans = seq[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + seq[i], seq[i])

    if i + 1 < n:
        dp[i][1] = max(dp[i - 1][1] + seq[i + 1], dp[i - 1][0] + seq[i])
    else:
        dp[i][1] = dp[i - 1][0] + seq[i]

    ans = max([ans, dp[i][1], dp[i][0]])

print(ans)