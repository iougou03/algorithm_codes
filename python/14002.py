n = int(input())
seq = list(map(int, input().split()))
dp = [1001 for _ in range(n + 1)]
dp_lis = [[] for _ in range(n + 1)]

def bsearch_lis(ni):
    global n

    idx = 1
    while idx <= n:
        if dp[idx] > seq[ni]:
            dp_lis[ni] = []
            dp[idx] = ni
            for i in range(idx):
                if seq[ni] > seq[i]:
                    dp_lis[ni].append(seq[i])
            return
        idx += 1

for i in range(n):
    bsearch_lis(i)

print(len(dp) -1)
print(dp_lis)
