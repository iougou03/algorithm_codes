# N = int(input())

# ans = [[0 for _ in range(11)] for __ in range(N + 1)]

# for i in range(1,10):
#     ans[1][i] = 1
# val = 1000000000

# test = N ; test_ans = 0
# def digit_reverse(n):
#     num = n
#     digit_list = []
#     while(num > 0):
#         digit_list.append(num % 10)
#         num //= 10
#     return digit_list

# for i in range(10**(test - 1),10**test):
#     dr = digit_reverse(i) ; status = True
#     if len(dr) > 1:
#         for j in range(1,len(dr)):
#             if abs(dr[j - 1] - dr[j]) != 1: 
#                 status = False
#                 break
#         if status:
#             print(i)
# print(ans[test])

# def solution(i, digit1):
#     if digit1 == 0: ans[i][digit1] = ans[i - 1][digit1 + 1]
#     else: ans[i][digit1] = ans[i - 1][digit1 + 1] + ans[i - 1][digit1 - 1] 
    
#     ans[i][digit1] %= val

# for i in range(2, N + 1):
#     for j in range(0,10):
#         solution(i,j)

# print(sum(ans[N]) % val)

# tried 2
M = 1000000000

n = int(input())
digit_dp = [[0 for _ in range(10)] for _ in range(n)]
digit_dp[0] = [1 if i != 0 else 0 for i in range(10)]

for d in range(1, n):
    for i in range(10):
        d1 = 0 ; d2 = 0
        if i - 1 >= 0: d1 = digit_dp[d - 1][i - 1]
        if i + 1 < 10: d2 = digit_dp[d - 1][i + 1]

        digit_dp[d][i] = d1 % M + d2 % M

ans = 0
for a in digit_dp[n - 1]:
    ans += a % M
print(ans % M)