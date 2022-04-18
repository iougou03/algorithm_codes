from collections import deque

direction = ((0,1), (1,0), (-1,0), (0,-1))

gx, gy = map(int, input().split())
goal = (gx - 1, gy - 1)
maze =[]

def bfs():
    queue = deque([(0,0)])

    while(queue):
        x,y = queue.popleft()
        
        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if 0<= nx < gx and 0<= ny < gy:
                if maze[nx][ny] == 1: 
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx,ny))

for _ in range(gx):
    maze.append(list(map(int, list(input()))))

bfs()

print(maze[goal[0]][goal[1]])


