from collections import deque
MAX_CNT = 51
direct = ((0, -1) , (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0))

n = int(input())
hex_board = []

locations = []

for y in range(n):
    hex_board.append(list(input()))
    for x in range(n):
        if hex_board[y][x] == 'X':
            locations.append([x, y])

color = [MAX_CNT for _ in range(n * n)]

visited = [0 for _ in range(n * n)]
def bfs(startx, starty):
    global MAX_CNT, n
    queue = deque([[startx, starty]])
    color_cnt = 0

    while queue:
        x, y = queue.popleft()

        if visited[y * n + x]: continue
        visited[y * n + x] = 1
        color_codes = []

        for dx, dy in direct:
            nx = dx + x ; ny = dy + y
            
            if 0 <= nx < n and 0 <= ny < n:
                if hex_board[ny][nx] == '-': continue
                
                if not visited[ny * n + nx]:
                    queue.append([nx, ny])
                
                if color[ny * n + nx] != MAX_CNT:
                    color_codes.append(color[ny * n + nx])
        
        code = 1
        while code in color_codes:
            code += 1

        color[y * n + x] = code
        color_cnt = max(color_cnt , code)
    
    return color_cnt

ans = 0
for x, y in locations:
    if not visited[y * n + x]:
        ans = max(ans, bfs(x, y))

if ans > 3: print(3)
else: print(ans)