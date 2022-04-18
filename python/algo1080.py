import sys

n, m = map(int, input().split())

a = [] ; b = [] 
ans = 0

for _ in range(n): a.append(list(map(int, list(input()))))
for _ in range(n): b.append(list(map(int, list(input()))))

# error code 2022/02/28

# direction = {
#     "rightBottom":[
#         ((-1,-1),
#         (-1,0),
#         (-1,1),),

#         ((-1,-1),
#         (0,-1),
#         (1,-1),)
#     ],
#     "leftTop":[
#         ((1,1),
#         (1,0),
#         (1,-1),),

#         ((-1,1),
#         (0,1),
#         (1,1))
#     ]
# }
# c = [[0 for _ in range(m)] for __ in range(n)]

# for i in range(n):
#     for j in range(m):
#         c[i][j] = 1 if a[i][j] == b[i][j] else 0

# def check_square(middlex, middley, d):
#     cnt = 0
#     for dx, dy in d[0]:
#         if not c[middley + dy][middlex + dx]: cnt += 1
#     if cnt >= 3: return True
#     cnt = 0
#     for dx, dy in d[1]:
#         if not c[middley + dy][middlex + dx]: cnt += 1
#     if cnt >= 3: return True

#     return False

# def active(middlex, middley):
#     for i in range(middley - 1, middley + 2):
#         for j in range(middlex - 1, middlex + 2):
#             c[i][j] = 0 if c[i][j] else 1

# def check_valid():
#     for i in range(n):
#         for j in range(m):
#             if not c[i][j]: return False
#     return True

# if n > 2 and m > 2:
#     for i in range(1, n - 1):
#         for j in range(1, m - 1):
#             if check_square(j,i,direction["rightBottom"]): 
#                 active(j,i)
#                 ans += 1

#     for i in range(n - 2, 0, -1):
#         for j in range(m - 2, 0, -1):
#             if check_square(j,i,direction["leftTop"]): 
#                 active(j,i)
#                 ans += 1

# # [print(line) for line in c]
# if check_valid(): print(ans)
# else: print(-1)

# version 1
def flip3x3(startx, starty,arr):
    for i in range(starty, starty + 3):
        for j in range(startx, startx + 3):
            arr[i][j] = 0 if arr[i][j] else 1

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]: 
            flip3x3(j,i,a)
            ans += 1

for i in range(2):
    for j in range(n):
        if a[j][m - 2 + i] != b[j][m - 2 + i]:
            print(-1)
            sys.exit(0)
    for j in range(m):
        if a[n - 2 + i][j] != b[n - 2 + i][j]:
            print(-1)
            sys.exit(0)

print(ans)