n = int(input())
matList = [0]

for _ in range(n):
    r, c = map(int, input().split())
    matList.append((r, c))

dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

for area in range(1, n):
    for start in range(1, n - area + 1):
        dp[start][start + area] = float("inf")
    
        for mid in range(start, start + area):
            newVal = matList[start][0] * matList[mid][1] * matList[start + area][1]
            dp[start][start + area] = min(dp[start][start + area], dp[start][mid] + dp[mid + 1][start + area] + newVal)

print(dp[1][n])

# -----------------------------------------------------

n = int(input())
matList = [0]

for _ in range(n):
    r, c = map(int, input().split())
    matList.append((r, c))

dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]

def sumMat(startIdx, endIdx):
    sumVal = 0
    mat = [matList[startIdx]]
    for i in range(startIdx, endIdx):
        sumVal += mat[0] * mat[1] * matList[i][1]
        mat[1] = matList[i][1]
    
    return sumVal

for end in range(1, n + 1):
    for start in range(1, end):
        dp[start][end] = float("inf")
    
        for mid in range(start, end):
            newVal = sumMat(start, mid)
            newVal += sumMat(mid + 1, end)

            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + newVal)

print(dp[1][n], dp)