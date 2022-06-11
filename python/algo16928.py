n, m = map(int , input().split())

ladder_coor = [0 for _ in range(101)]
snake_coor = [0 for _ in range(101)]

for _ in range(n):
    x, y = map(int , input().split())
    ladder_coor[x] = y

for _ in range(m):
    u, v = map(int , input().split())
    snake_coor[u] = v

visited = [0 for _ in range(101)]
ans = 101

def bfs(start , end):
    queue = deque([[start, 0]])

    while queue:
        node, cnt = queue.popleft()

        if node == end: return cnt

        if visited[node]: continue
        visited[node] = 1
        
        for i in range(1, 7):
            nn = node + i
            if nn > 100: continue
            
            if ladder_coor[nn]: nn = ladder_coor[nn]
            elif snake_coor[nn]: nn = snake_coor[nn]
            
            queue.append([nn, cnt + 1])

print(bfs(1, 100))

