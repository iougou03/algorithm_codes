# n = int(input())

# direct = [[0,1],[0,-1],[1,0],[-1,0]]
# matrix = []
# visited = []
# areas = []

# def bfs(start_x,start_y):
#     stack = [[start_x ,start_y]]
#     cnt = 0
    
#     while(stack):
#         x,y = stack.pop()
        
#         if(visited[y][x]): continue
#         visited[y][x] = 1 ; cnt += 1
 
#         for dx, dy in direct:
#             nx = x + dx
#             ny = y + dy
#             if(0<= nx < n and 0<= ny < n):
#                 if(matrix[ny][nx]): stack.append([nx,ny])
#     return cnt

# for i in range(n):
#     matrix.append(list(map(int, list(input()))))
#     visited.append([0 for _ in range(len(matrix[i]))])

# for i in range(n):
#     for j in range(n):
#         if(not matrix[i][j]): continue
#         cnt = bfs(j,i)
#         if(cnt): areas.append(cnt)

# areas.sort()

# print(len(areas))
# [print(i) for i in areas]


# import random
# l = set()

# for _ in range(20): 
#     l.add(int(random.random() * 100))

# l = list(l)
# l.sort()
# print(l)

# def bsearch(arr,search_val):
#     left = 0 ; right = len(arr) - 1

#     while(left <= right):
#         middle = (left + right) // 2
#         if search_val < arr[middle]: right = middle - 1
#         elif search_val > arr[middle]: left = middle + 1
#         else: return middle
    
#     return -1

# print("enter searching number : ", end="")
# n = int(input())
# print(bsearch(l, n))


def callStack(n):
    if n == 1: return
    callStack(n - 1)
    print(n)

callStack(5)