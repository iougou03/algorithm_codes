t = int(input())
ans_list = []

def nCm(n, m):
    ans = 1
    s1 = max(n, m - n)
    s2 = min(n, m - n)
    for i in range(s1 + 1,m + 1): ans *= i
    for j in range(1, s2 + 1): ans //= j
    
    return ans

for _ in  range(t):
    n, m = map(int, input().split())
    ans_list.append(nCm(n, m))

[print(a) for a in ans_list]