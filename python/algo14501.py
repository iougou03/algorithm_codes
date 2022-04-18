# n = int(input())

# ans = 0
# reservateHelps = [[0, 0] for _ in range(n + 1)]

# for i in range(n):
#     t, p = map(int, input().split())
#     reservateHelps[i + 1][0] = t
#     reservateHelps[i + 1][1] = p


# def solution(days, pay):
#     global ans, n
#     if days == n + 1: 
#         ans = max(ans, pay)
#         return
#     if days > n + 1: return

#     solution(days + reservateHelps[days][0], pay + reservateHelps[days][1])
#     solution(days + 1, pay)

# solution(1, 0)

# print(ans)

# ------------------------------------------------------------------------ #

# n = int(input())

# ansList = []
# reservateHelps = [[0, 0] for _ in range(n + 1)]

# for i in range(n):
#     t, p = map(int, input().split())
#     reservateHelps[i + 1][0] = t
#     reservateHelps[i + 1][1] = p

# ans = 0
# def solution(days, pay):
#     global ans
#     for i in range(days, n + 1):
#         nextDay = i + reservateHelps[i][0]
#         if nextDay > n + 1:
#             ans = max(ans, pay)
#         elif nextDay == n + 1:
#             ans = max(pay + reservateHelps[i][1] , ans)
#         else:
#             solution(nextDay, pay + reservateHelps[i][1])

# solution(1, 0)

# print(ans)