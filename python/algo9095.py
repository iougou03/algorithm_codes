# import sys
# input = sys.stdin.readline

# t = int(input())
# ans = 0

# def rec(n, end):
#     global ans
#     if n == end:
#         ans += 1
#         return
#     elif n > end: return

#     rec(n + 1, end)
#     rec(n + 2, end)
#     rec(n + 3, end)

# for _ in range(t):
#     n = int(input())
#     rec(0 , n)
#     print(ans)
#     ans = 0

import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(11)]
dp[1] = 1 ; dp[2] = 2 ; dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])
