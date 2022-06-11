from collections import deque

night = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))

n = int(input())

board = [[0] * n for _ in range(n)]
startx, starty, endx, endy = map(int , input().split())

def bfs(startx, starty, endx, endy, n):
    queue = deque([[startx, starty, 0]])
    visited = [0 for _ in range(n * n)]

    while queue:
        x, y, cnt = queue.popleft()

        if visited[y * n + x]: continue
        visited[y * n + x] = 1

        for dx , dy in night:
            nx = dx + x ; ny = dy + y
            
            if (0 <= nx < n and 0 <= ny < n):
                if ny == endy and nx == endx:
                    return cnt + 1
                if not visited[ny * n + nx]:
                    queue.append([nx , ny, cnt + 1])

    return -1
print(bfs(startx, starty, endx, endy, n))