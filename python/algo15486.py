import sys

input = sys.stdin.readline
n = int(input())
inputList = [0]

for i in range(n):
    t, p = map(int, input().split())

    inputList.append([t, p]) # Ti, Pi, EndDay

dp = [0 for _ in range(n + 2)] # sumP, lastEndDay

def maxVal(a, b):
    return a if a > b else b

maxSum = 0 ; ans = 0
for i in range(1, n + 1):
    maxSum = maxVal(maxSum, dp[i])
    nextIdx = i + inputList[i][0]

    if nextIdx <= n + 1:
        dp[nextIdx] = maxVal(maxSum + inputList[i][1], dp[nextIdx])
        ans = max(ans, dp[nextIdx])

print(ans)