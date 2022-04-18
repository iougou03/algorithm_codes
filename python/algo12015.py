n = int(input())
seq = list(map(int, input().split()))
binary_dp = [0]

def LIS_binary(num):
    left = 0 ; right = len(binary_dp) - 1

    while left <= right:
        middle = (left + right) // 2

        if binary_dp[middle] < num: left = middle + 1
        elif binary_dp[middle] > num: right = middle - 1
        else:
            left = middle
            break

    if left >= len(binary_dp):
        binary_dp.append(num)
    elif binary_dp[left] > num: 
        binary_dp[left] = num

for s in seq: LIS_binary(s)

print(len(binary_dp) - 1)