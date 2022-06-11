MAX_VAL = 1000001

n = int(input())

seq = list(map(int, input().split()))

dp = []

for i in range(n):
    v = seq[i]

    if not dp: dp.append(v)
    else:
        left = 0 ; right = len(dp) - 1
        
        while left <= right:
            middle = (left + right) // 2

            if dp[middle] > v: left = middle + 1
            else: right = middle - 1
        
        if left == len(dp): dp.append(v)
        elif dp[left] < v: dp[left] = v

print(len(dp))

