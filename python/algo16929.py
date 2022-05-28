from collections import deque
import sys
input = sys.stdin.readline

direction = ((0, 1), (1, 0), (-1, 0), (0, -1))

n, m = map(int, input().split())

gameBoard = []
for i in range(n):
    gameBoard.append(list(input())[:-1])

def bfs_cycle(startx, starty):
    global n, m
    initColor = gameBoard[starty][startx]

    queue =  deque([(startx, starty, 0, 0)])
    visited = [0 for _ in range(n * m)]

    while queue:
        x, y, px, py = queue.popleft()

        if visited[x + y * m]: continue
        visited[x + y * m] = 1

        for dx, dy in direction:
            nx = dx + x ; ny = dy + y
            if 0<=nx<m and  0<=ny<n:
                if gameBoard[ny][nx] != initColor: continue

                if (nx != px and ny != py) and visited[nx + ny * m]: return True

                if not visited[nx + ny * m]:
                    queue.append((nx, ny, x, y))

    return False

for y in range(n):
    for x in range(m):
        if bfs_cycle(x, y):
            print("Yes")
            sys.exit(0)

print("No")