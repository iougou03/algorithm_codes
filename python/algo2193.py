n = int(input())
dp_pnums = [[0 for _ in range(2)] for _ in range(n + 1)]
dp_pnums[1][1] = 1
if n > 1:
    dp_pnums[2][0] = 1
if n > 2:
    dp_pnums[3][0] = 1
    dp_pnums[3][1] = 1

for i in range(4, n + 1):
    dp_pnums[i][0] = dp_pnums[i - 1][1] + dp_pnums[i - 1][0]
    dp_pnums[i][1] = dp_pnums[i - 1][0]

print(sum(dp_pnums[n]))

# 1

# 10

# 101
# 100
# (8 4 2 1)

# 1010
# 1001
# 1000
# 2^3 2^1
# << = x2
# dp[4][0] = dp[3][1] + dp[3][0]
# dp[4][1] = dp[3][0]
