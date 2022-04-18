n, k = map(int,input().split())

def nCk2(n, k):
    ans = 1
    for i in range(1, n + 1): ans *= i % 10007
    for i in range(1, n - k + 1): ans //= i % 10007
    for i in range(1, k + 1): ans //= i % 10007

    print(ans % 10007)

nCk2(n, k)