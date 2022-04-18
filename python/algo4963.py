from collections import deque

direction = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

def bfs(arr, visited, startx, starty, w, h):
    queue = deque([[startx , starty]])

    while queue:
        cx, cy = queue.popleft()
        if visited[cy * w + cx]: continue
        visited[cy * w + cx] = 1

        for dx, dy in direction:
            nx = cx + dx ; ny = cy + dy
            if 0<= nx < w and 0<= ny < h:
                idx = ny * w + nx
                if arr[ny][nx] and not visited[idx] : queue.append([nx, ny])
    
def solution(arr, w, h):
    visited = [0 for _ in range(w * h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            idx = i * w + j
            if arr[i][j] and not visited[idx]: 
                bfs(arr, visited, j, i, w, h)
                cnt += 1
    return cnt

ans = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break

    land_map = []
    for _ in range(h): 
        land_map.append(list(map(int, input().split())))

    ans.append(solution(land_map, w, h))

[print(a) for a in ans]