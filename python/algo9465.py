t = int(input())

for _ in range(t):
    n = int(input())

    dp = [[0, 0] for _ in range(n + 1)]
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int , input().split())))
    
    dp[1][0] = stickers[0][0]
    dp[1][1] = stickers[1][0]

    for i in range(2, n + 1):
        dp[i][0] = max(max(dp[i - 2]), dp[i - 1][1]) + stickers[0][i - 1]
        dp[i][1] = max(max(dp[i - 2]), dp[i - 1][0]) + stickers[1][i - 1]
    
    print(max(dp[n]))

    