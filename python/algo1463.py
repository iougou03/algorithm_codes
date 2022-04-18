N = int(input())
nums = [0 for _ in range(N + 1)]
nums[1] = 0

for i in range(2, N + 1):
    val = 1000000
    if i % 3 == 0: val = min(val, nums[i // 3])
    if i % 2 == 0: val = min(val, nums[i // 2])
    val = min(val, nums[i - 1])
    nums[i] = val + 1

print(nums[N])