A = [] ; B = [] 

N, M = map(int, input().split())
for _ in range(N): A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for _ in range(M): B.append(list(map(int, input().split())))

C = [[0 for _ in range(K)] for __ in range(N)]

# version1
# for i in range(N):
#     for j in range(K):
#         for m in range(M):
#             C[i][j] += A[i][m] * B[m][j]
    

for c in C:
    [print(num, end=" ") for num in c]
    print()

