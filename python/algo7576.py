# version 1.

# from collections import deque
# import sys

# direction = ((0,1), (1,0), (0,-1), (-1,0))
# # 하루가 지나면 주위 토마토가 익음
# # 칸에 일수를 기록하자, 같은 siblings은 같은 일수를 가져야하므로, BFS를 사용
# # 다음 칸으로 이동할 때 다음칸(v(n + 1))이 자신(v(n) + 1)보다 크다면, 이동 그리고 자신의 것으로 덮어씌움
# # 1. -1은 다음 경로에 추가하지 않음
# # 2. 0 은 익지 않은 토마토므로 조회해서 자신을 것을 더함
# # 3. 익었는데 만약 더 짧은 날짜가 가능한게 있다면 최신화
# # 모든 칸을 조회해보며 가장 큰 날짜를 출력
# # O(M × N)

# M, N = map(int , sys.stdin.readline().split())
# matrix = [] ; ans = 0 ; ripes = []

# def bfs():
#     queue = deque(ripes)

#     while(queue):
#         cx, cy = queue.popleft()
#         for dx, dy in direction:
#             nx = dx + cx
#             ny = dy + cy
#             if 0<= nx < M and 0<= ny < N:
#                 if matrix[ny][nx] == -1 or matrix[ny][nx] == 1: continue
#                 elif matrix[ny][nx] == 0:
#                     matrix[ny][nx] = matrix[cy][cx] + 1
#                     queue.append([nx,ny])
#                 elif matrix[ny][nx] > 1 and matrix[ny][nx] > matrix[cy][cx] + 1:
#                     matrix[ny][nx] = matrix[cy][cx] + 1
#                     queue.append([nx,ny])


# for y in range(N):
#     matrix.append(list(map(int, sys.stdin.readline().split())))
#     for x in range(M):
#         if matrix[y][x] == 1: ripes.append([x,y])

# bfs()

# for m in matrix: 
#     if 0 in m: 
#         ans = 0
#         break
#     ans = max(ans, max(m)) 

# # [print(m) for m in matrix]
# print(ans - 1)


# version 2.
from collections import deque
import sys

direction = ((0,1), (1,0), (0,-1), (-1,0))
M, N = map(int , sys.stdin.readline().split())
matrix = [] ; ripes = [] ; totmato_cnt = N * M

def bfs(totmato_cnt):
    ans = 0 ; cnt = 0
    queue = deque(ripes)

    while(queue):
        cnt += 1
        cx, cy = queue.popleft()

        for dx, dy in direction:
            nx = dx + cx
            ny = dy + cy
            if 0<= nx < M and 0<= ny < N:
                if matrix[ny][nx] == -1 and matrix[ny][nx] == 1: continue
                elif matrix[ny][nx] == 0:
                    matrix[ny][nx] = matrix[cy][cx] + 1
                    queue.append([nx,ny])
                    ans = max(matrix[ny][nx], ans)

    if cnt != totmato_cnt: return -1
    elif ans == 0: return 0
    else: return ans - 1

for y in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    for x in range(M):
        if matrix[y][x] == 1: ripes.append([x,y])
        elif matrix[y][x] == -1: totmato_cnt -= 1

print(bfs(totmato_cnt))
# [print(m) for m in matrix]

