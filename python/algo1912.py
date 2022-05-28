n = int(input())
seq = list(map(int, input().split()))
dp = [0 for _ in range(n)]
ans = -1001

for i in range(n):
    if seq[i] > dp[i - 1] + seq[i]:
        dp[i] = seq[i]
    else:
        dp[i] = dp[i - 1] + seq[i]
    
    ans = max(ans, dp[i])

print(ans)
