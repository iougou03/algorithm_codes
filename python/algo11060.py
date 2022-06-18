n = int(input())
seq = list(map(int , input().split()))

dp = [1001] * (n + 1)
dp[1] = 0

for i in range(n):
    for v in range(1, seq[i] + 1):
        if i + v + 1 > n: continue
        dp[i + v + 1] = min(dp[i + v + 1], dp[i + 1] + 1)

if dp[n] < 1001:
    print(dp[n])
else: 
    print(-1)