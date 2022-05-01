# N = int(input())
# nums = [0 for _ in range(N + 1)]
# nums[1] = 0

# for i in range(2, N + 1):
#     val = 1000000
#     if i % 3 == 0: val = min(val, nums[i // 3])
#     if i % 2 == 0: val = min(val, nums[i // 2])
#     val = min(val, nums[i - 1])
#     nums[i] = val + 1

# print(nums[N])

# -------------------------

n = int(input())
dp = [0 for _ in range(n + 1)]
dp[n] = 0

for i in range(n - 1, 0, -1):
    val = dp[i + 1]
    if i * 3 <= n:
        val = min(val, dp[i * 3])
    if i * 2 <= n:
        val = min(val, dp[i * 2])
    
    dp[i] = val + 1

print(dp[1])