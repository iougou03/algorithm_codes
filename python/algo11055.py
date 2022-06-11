n = int(input())

seq = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = seq[0]
ans = dp[0]

for i in range(1, n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j])
    
    dp[i] += seq[i]
    ans = max(ans, dp[i])

print(ans)