import sys

input = sys.stdin.readline
n, k = map(int, input().split())
stuff = [0]
vals = [[-1 for _ in range(k + 1)] for __ in range(n + 1)]

for i in range(n):
    w, v = map(int, input().split())
    stuff.append([v, w])

def knapsack(i, weight):
    if i < 1: return 0

    if vals[i][weight] == -1:
        if stuff[i][1] > weight:
            vals[i][weight] = knapsack(i - 1, weight)
        else:
            vals[i][weight] = max(knapsack(i - 1, weight), knapsack(i - 1, weight - stuff[i][1]) + stuff[i][0])

    return vals[i][weight]
# ans = 0
# for i in range(1, n + 1):
#     for j in range(k, 0, -1):
#         if j - stuff[i][1] < 0: break
#         vals[j] = max(vals[j], vals[j - stuff[i][1]] + stuff[i][0])
#         ans = max(vals[j], ans)
print((knapsack(n, k)))

# vals = [0 for _ in range(k + 1)] 
# idx = 0 ; totalV = 0
# ans = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:continue
#         if i + j <= k:
#             vals[i + j]

# # print(ans , vals)
