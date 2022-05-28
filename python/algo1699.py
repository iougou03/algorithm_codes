n = int(input())
dp = [i for i in range(n + 1)]
sq = [i * i for i in range(1, 317)]

for i in range(1, n + 1):
    for j in sq:
        if j > i: break
        dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[n])