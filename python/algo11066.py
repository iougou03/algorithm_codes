t = int(input())

ans = []
for _ in range(t):
    k = int(input())
    paperList = [0] + list(map(int, input().split()))
    
    sumList = [0 for _ in range(k + 1)]
    val = 0
    for i in range(1, k + 1):
        val += paperList[i]
        sumList[i] = val
    dp = [[0 for _ in range(k + 1)] for __ in range(k + 1)]
    
    
    for d in range(1, k):
        for start in range(1, k + 1 - d):
            end = start + d
            dp[start][end] = float("inf")

            for mid in range(start, end):
                print(start, mid," ",mid + 1, end)
                print(dp[start][mid], dp[mid + 1][end], sumList[end] - sumList[start - 1])
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + sumList[end] - sumList[start - 1])
            
            print(start, dp)
    
    ans.append(dp[1][k])

[print(a) for a in ans]



# 1 ~ k -> even
# dp[1][k] = dp[i][middle] + dp[middle + 1][k]

# 1 ~ k -> odd
# dp[1][k] = max(dp[i][middle] + dp[middle + 1][k], dp[middle + 1][k] + dp[middle + 2][k])