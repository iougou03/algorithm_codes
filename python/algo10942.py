import sys
input = sys.stdin.readline

n = int(input())
numList = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1): dp[i][i] = 1

for i  in range(1 , n): 
    if numList[i] == numList[i + 1]: dp[i][i + 1] = 1

for gap in range(2, n): # s - e = 1 ~ n - 1
    for i in range(1, n - gap + 1):
        if numList[i] == numList[i + gap] and dp[i + 1][i + gap - 1]:
            dp[i][i + gap] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])