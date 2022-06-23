from collections import deque

direction = ((0, -1), (-1, 0), (1, 0), (0, 1))

n = int(input())
space = []
startCoor = []
sharkInitSize = 2
fishCnt = 0

for y in range(n):
    space.append(list(map(int, input().split())))
    for x in range(n):
        if space[y][x] == 9: startCoor = [x, y]
        elif space[y][x] > 0: fishCnt += 1

def printSpace(x, y):
    for i in range(len(space)):
        for j in range(len(space)):
            if i == y and j == x:
                print(f"*{space[i][j]}*", end=" ")
            else: print(space[i][j], end=" ")
        print()
    print()

def sharkBfs(startx, starty, startSize, n, fishCnt):
    queue = deque([[startx, starty, 0]])
    visited = [0 for _ in range(n * n)]
    seconds = 0
    size = startSize ; sizeCnt = startSize
    space[starty][startx] = 0
    distList = []

    while fishCnt > 0 and queue:

        while queue:
            x, y, cnt = queue.popleft()

            if visited[y * n + x]: continue
            visited[y * n + x] = 1

            for dx, dy in direction:
                nx = x + dx ; ny = y + dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[ny * n + nx]: continue

                    if space[ny][nx] == 0:
                        queue.append([nx, ny, cnt + 1])
                    else: # if fish is exist
                        if space[ny][nx] < size:
                            distList.append([nx,ny,cnt + 1])
                            break
                        elif space[ny][nx] == size:
                            queue.append([nx, ny, cnt + 1])
                        else: pass

        if not distList: continue
        
        
        distList.sort(key = lambda x:x[0])
        distList.sort(key = lambda x:x[1])
        distList.sort(key = lambda x:x[2])
        
        shortestPath = distList[0]

        fishCnt -= 1
        seconds += shortestPath[2]
        space[shortestPath[1]][shortestPath[0]] = 0
        sizeCnt -= 1
        if sizeCnt == 0: size += 1 ; sizeCnt = size
        
        shortestPath[2] = 0
        visited = [0 for _ in range(n * n)]
        distList = []
        queue.append(shortestPath)
        
        # printSpace(shortestPath[0], shortestPath[1])

    return seconds

print(sharkBfs(startCoor[0], startCoor[1], sharkInitSize, n, fishCnt))