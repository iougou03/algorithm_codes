import sys

N, B = map(int, sys.stdin.readline().split())
matrix = [] ; ans = []
mod = 1000

def squareMatrixMultiplation(a,b):
    global mod, N
    c = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= mod
    
    return c

for i in range(N):
    line = list(map(int, sys.stdin.readline().split())) 
    matrix.append(line)
    ans.append([0 for _ in range(N)])
    ans[i][i] = 1

while B > 0:
    if B % 2 == 1: ans = squareMatrixMultiplation(ans,matrix)
    matrix = squareMatrixMultiplation(matrix, matrix)
    B //= 2

for line in ans:
    [print(a, end=" ") for a in line]
    print()