from enum import Enum

class Command(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

n = int(input())

board2048 = [list(map(int , input().split())) for _ in range(n)]

def copyBoard(board:list):
    return [line.copy() for line in board]

def move(board:list, command:Command):
    row = len(board)
    col = len(board[0])
    
    # preprocessing for merging each other
    if command.value[0]:
        c1 = 1 ; c2 = -command.value[0]
    else:
        c1 = -command.value[1] ; c2 = 1

    if command.name == "UP":
        ystart = 0 ; yend = row
    elif command.name == "DOWN":
        ystart = row - 1 ; yend = -1
    else:
        ystart = 0 ; yend = row

    if command.name == "LEFT":
        xstart = 0 ; xend = col
    elif command.name == "RIGHT":
        xstart = col - 1 ; xend = -1
    else:
        xstart = 0 ; xend = col

    for y in range(ystart, yend, c1):
        for x in range(xstart ,xend, c2):
            dx, dy = command.value
            cx = x ; cy = y

            while board[cy][cx] > 0:
                nx = dx + cx ; ny = dy + cy
                if 0 > nx or nx >= col or 0 > ny or ny >= row: break
                if board[ny][nx] != 0: break
                
                board[ny][nx] = board[cy][cx]
                board[cy][cx] = 0

                cy = ny ; cx = nx

    for y in range(ystart, yend, c1):
        for x in range(xstart ,xend, c2):
            if board[y][x] > 0:
                dx, dy = command.value
                nx = dx + x ; ny = dy + y
                if 0 > nx or nx >= col or 0 > ny or ny >= row: continue
                
                if board[ny][nx] == board[y][x]:
                    board[ny][nx] += board[y][x]
                    board[y][x] = 0
                
    # actual move
    for y in range(ystart, yend, c1):
        for x in range(xstart ,xend, c2):
            dx, dy = command.value
            cx = x ; cy = y

            while board[cy][cx] > 0:
                nx = dx + cx ; ny = dy + cy
                if 0 > nx or nx >= col or 0 > ny or ny >= row: break
                if board[ny][nx] != 0: break
                
                board[ny][nx] = board[cy][cx]
                board[cy][cx] = 0

                cy = ny ; cx = nx

#     print(command.name)
#     printBoard(board)
#     print("-------------------")

# def printBoard(board):
#     [print(*line) for line in board]
#     print()

ans = 0
def solution(command:Command, board:list, cnt:int):
    global ans
    if cnt == 6:
        ans = max(max([max(line) for line in board]), ans)
        return
    
    cb = copyBoard(board)
    move(cb, command)

    for com in Command:
        solution(com, cb, cnt + 1)

for com in Command:
    solution(com, board2048, 1)

print(ans)