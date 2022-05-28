n = int(input())
seq = list(map(int, input().split()))
dp_lis = [[] for _ in range(n)]
ans = [0, []]

for i in range(n):
    dp_lis[i] = [seq[i]]
    for j in range(i):
        if seq[j] < seq[i]:
            if len(dp_lis[i]) < len(dp_lis[j]) + 1:
                dp_lis[i] = dp_lis[j] + [seq[i]]

    if ans[0] < len(dp_lis[i]):
        ans[0] = len(dp_lis[i])
        ans[1] = dp_lis[i]

print(ans[0])
print(*ans[1])