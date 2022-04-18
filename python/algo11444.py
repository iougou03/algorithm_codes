mod = 1000000007
n = int(input())

def fibo_div(a, b):
    c=[[0, 0],[0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= mod
    return c

ans = [
    [1,0],
    [0,1]
]
a = [
    [1,1],
    [1,0]
]

while n > 0:
    if n % 2 == 1:
        ans = fibo_div(ans  ,a)
    a = fibo_div(a,a)
    n //= 2

print(ans[0][1])