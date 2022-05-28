n = int(input())

MAX_NUM = 10000000
plist = list(map(int, input().split()))
dp = [MAX_NUM for _ in range(n + 1)]
dp[0] = 0 ; dp[1] = plist[0]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + plist[j - 1])

print(dp[n])