MAX_NUM = 1000001

n = int(input())

house = []

for _ in range(n):
    house.append(list(map(int, input().split())))

dp = [[[MAX_NUM] * 3 for _ in range(3)] for _ in range(n)]

dp[0][0][0] = house[0][0]
dp[0][1][1] = house[0][1]
dp[0][2][2] = house[0][2]

for i in range(1, n):
    dp[i][0][0] = min(dp[i - 1][0][1], dp[i - 1][0][2]) + house[i][0]
    dp[i][0][1] = min(dp[i - 1][0][0], dp[i - 1][0][2]) + house[i][1]
    dp[i][0][2] = min(dp[i - 1][0][1], dp[i - 1][0][0]) + house[i][2]
    
    dp[i][1][0] = min(dp[i - 1][1][1], dp[i - 1][1][2]) + house[i][0]
    dp[i][1][1] = min(dp[i - 1][1][0], dp[i - 1][1][2]) + house[i][1]
    dp[i][1][2] = min(dp[i - 1][1][1], dp[i - 1][1][0]) + house[i][2]
    
    dp[i][2][0] = min(dp[i - 1][2][1], dp[i - 1][2][2]) + house[i][0]
    dp[i][2][1] = min(dp[i - 1][2][0], dp[i - 1][2][2]) + house[i][1]
    dp[i][2][2] = min(dp[i - 1][2][0], dp[i - 1][2][1]) + house[i][2]

ans = MAX_NUM

for i in range(3):
    for j in range(3):
        if i == j: continue
        ans = min(ans, dp[n - 1][i][j])
print(ans)