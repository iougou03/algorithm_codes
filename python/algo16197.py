from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

n, m = map(int, input().split())
board = []

c1 = None ; c2 = None
spaceCnt = 0

for y in range(n):
    board.append(input())

    for x in range(m):
        if board[y][x] == "o": 
            if not c1: c1 = [x, y]
            else: c2 = [x, y]
        
        else: spaceCnt += 1

ans = 11

def can_locate(x, y):
    global n, m
    return True if 0<= x < m and 0<= y < n else False

def solution(command, coor1, coor2, cnt):
    global ans
    if cnt >= ans: return

    dx, dy = direction[command]

    x1 = coor1[0] + dx ; y1 = coor1[1] + dy
    x2 = coor2[0] + dx ; y2 = coor2[1] + dy

    cnt += 1
    if can_locate(x1, y1) and can_locate(x2, y2):
        if board[y1][x1] == "#":
            x1 -= dx ; y1 -= dy
        if board[y2][x2] == "#":
            x2 -= dx ; y2 -= dy

        for i in range(4): solution(i, [x1, y1], [x2, y2], cnt)

    elif can_locate(x1, y1) or can_locate(x2, y2):
        ans = min(ans, cnt)
    
    else: return

for i in range(4): solution(i, c1, c2, 0)
print(ans if ans <= 10 else -1)