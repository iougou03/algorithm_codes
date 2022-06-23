from collections import deque

direction = ((1, 0), (-1, 0), (0, -1), (0, 1))

n = int(input())
image = []

for i in range(n):
    image.append(list(input()))

visited1 = [0] * (n * n)
visited2 = [0] * (n * n)

def bfs(startx:int, starty:int, n:int, colorList:list, board:list, visited:list):
    queue = deque([[startx, starty]])
    
    while queue:
        x, y = queue.popleft()

        if visited[y * n + x]: continue
        visited[y * n + x] = 1

        for dx, dy in direction:
            nx = dx + x ; ny = dy + y

            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny * n + nx]: continue

                if board[ny][nx] in colorList:
                    queue.append([nx, ny])

ans = 0
cbans = 0

for y in range(n):
    for x in range(n):
        if not visited1[y * n + x]:
            if image[y][x] == 'R' or image[y][x] == 'G':
                bfs(x, y, n, ['R', 'G'], image, visited1)
            else:
                bfs(x, y, n, [image[y][x]], image, visited1)
            cbans += 1
            
        if not visited2[y * n + x]:
            bfs(x, y, n, [image[y][x]], image, visited2)
            ans += 1

print(ans, cbans)