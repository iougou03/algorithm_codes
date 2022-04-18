from collections import deque

direction = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))

T = int(input())

def bfs(current_x, current_y, goal_x, goal_y, I):
    chess = [[0 for _ in range(I)] for __ in range(I)]
    queue = deque([(current_x, current_y)])

    while queue:
        x,y = queue.popleft()
        
        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if 0<= nx < I and 0 <= ny < I:
                if ny == goal_y and nx == goal_x:
                    return chess[y][x] + 1
                if chess[ny][nx] == 0:
                    chess[ny][nx] = chess[y][x] + 1
                    queue.append((nx,ny))

ans = []

for _ in range(T):
    I = int(input())
    current_x, current_y = map(int, input().split())
    goal_x, goal_y= map(int, input().split())
    if (current_y == goal_y and current_x == goal_x):
        ans.append(0)
        continue
    ans.append(bfs(current_x, current_y, goal_x, goal_y,I))

[print(a) for a in ans]
    
