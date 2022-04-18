import sys
from collections import deque

direction = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1))
M, N, H = map(int, sys.stdin.readline().split())

def valid(ni, max_val):
    return 0 <= ni < max_val

def bfs(start_list, total_cnt):
    ans = 0
    queue = deque(start_list) ; cnt = len(start_list)
    
    while(queue):
        z, x ,y= queue.popleft()

        for dz, dx, dy in direction:
            nx = x + dx ; ny = y + dy ; nz = z + dz
            if valid(nx, M) and valid(ny, N) and valid(nz, H) and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx]  = tomato[z][y][x] + 1
                ans = max(ans, tomato[nz][ny][nx])
                queue.append([nz,nx,ny])
                cnt += 1

    if cnt != total_cnt: return -1
    else: return ans - 1
    
tomato = [] ; tomato_cnt = M * N * H
ripes = [] ; ripes_cnt = 0

for h in range(H):
    tomato.append([])

    for y in range(N):
        tomato[h].append(list(map(int, sys.stdin.readline().split())))
        for x in range(M):
            if tomato[h][y][x] == 1:
                ripes.append([h, x, y])
                ripes_cnt += 1
            elif tomato[h][y][x] == -1: tomato_cnt -= 1

if ripes_cnt == tomato_cnt:
    print(0)
else:
    print(bfs(ripes, tomato_cnt))

# for square in tomato:
#     [print(s) for s in square]
#     print()