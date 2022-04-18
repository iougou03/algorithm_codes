n, k = map(int, input().split())
numList = []
# store for how many ways can make the natural number i
make_i_dp = [0 for _ in range(k + 1)]
# when we didn't use any coins, we can get zero
make_i_dp[0] = 1

for i in range(n):
    numList.append(int(input()))

for num in numList:
    for j in range(num, k + 1):
        make_i_dp[j] += make_i_dp[j - num]

print(make_i_dp[-1])