# import sys

# N = int(sys.stdin.readline())
# rgbs = [[0, 0, 0]]
# mask = [[0, 0, 0]]

# def solution():

#     for i in range(1, N + 1):
#         mask[i][0] = min(mask[i - 1][1] , mask[i - 1][2]) + rgbs[i][0]
#         mask[i][1] = min(mask[i - 1][0] , mask[i - 1][2]) + rgbs[i][1]
#         mask[i][2] = min(mask[i - 1][0] , mask[i - 1][1]) + rgbs[i][2]

#     return mask[-1]

# for _ in range(N):
#     rgbs.append(list(map(int, sys.stdin.readline().split())))
#     mask.append([0, 0, 0])

# print(min(solution()))


# def dfs(prev_color, price, level):
#     global ans
#     if level == N: 
#         ans = min(ans, price)
#         return

#     price += rgbs[level][prev_color]

#     for i in range(3): 
#         if prev_color == i: continue
#         dfs(i,price,level + 1)

# uncorrect : timeout - 경우의 수가 너무 많아서 틀림
# dfs(0, 0, 0)
# dfs(1, 0, 0)
# dfs(2, 0, 0)

# def solution():
#     mask = [
#             [0, rgbs[0][0]], 
#             [1, rgbs[0][1]], 
#             [2, rgbs[0][2]]
#         ] # prev color, price

#     for i in range(1, N):
#         val0 = 1000 ; val1 = 1000 ; val2 = 1000 
#         idx0 = mask[0][0] ; idx1 = mask[1][0] ; idx2 = mask[2][0]

#         for j in range(3):
#             if j != mask[0][0]: 
#                 idx0 = idx0 if val0 < rgbs[i][j] else j
#                 val0 = min(val0, rgbs[i][j])
#             if j != mask[1][0]: 
#                 idx1 = idx1 if val0 < rgbs[i][j] else j
#                 val1 = min(val1, rgbs[i][j])
#             if j != mask[2][0]: 
#                 idx2 = idx2 if val0 < rgbs[i][j] else j
#                 val2 = min(val2, rgbs[i][j])
#         print(i, val0, val1, val2)
#         mask[0][0] = idx0
#         mask[1][0] = idx1
#         mask[2][0] = idx2
#         mask[0][1] += val0
#         mask[1][1] += val1
#         mask[2][1] += val2

#     return mask
# uncorrect : logical error - 논리가 틀림(아예 틀린 정답)

# 2022 05 10
import sys
input = sys.stdin.readline

n = int(input())
house = []
dp = [[0]*3 for _ in range(n)]

for i in range(n):
    house.append(list(map(int, input().split())))

dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][2]

print(min(dp[n - 1]))
