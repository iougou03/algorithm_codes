direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

n, m = map(int, input().split())

board = []
blue_coor = [0, 0]
red_coor = [0, 0]

for y in range(n):
    line = list(input())

    board.append(line)
    for x in range(m):
        if board[y][x] == "B": blue_coor = [x, y]
        elif board[y][x] == "R": red_coor = [x, y]

ans = 11
visited = [[0] * m for _ in range(n)]

def isSpace(x, y):
    return True if board[y][x] != "#" else False

def move(dx:int, dy:int, redx:int, redy:int, bluex:int, bluey:int, cnt:int):
    global ans
    falled = False

    while board[redy + dy][redx + dx] == ".":
        board[redy + dy][redx + dx] = "R"
        board[redy][redx] = "."
        redy += dy ; redx += dx

    while board[bluey + dy][bluex + dx] == ".":
        board[bluey + dy][bluex + dx] = "B"
        board[bluey][bluex] = "."
        bluey += dy ; bluex += dx

    while board[redy + dy][redx + dx] == ".":
        board[redy + dy][redx + dx] = "R"
        board[redy][redx] = "."
        redy += dy ; redx += dx

    if board[redy + dy][redx + dx] == "O":
        board[redy][redx] = "."
        falled = True

        while board[bluey + dy][bluex + dx] == ".":
            board[bluey + dy][bluex + dx] = "B"
            board[bluey][bluex] = "."
            bluey += dy ; bluex += dx

        if board[bluey + dy][bluex + dx] != "O":
            ans = min(ans, cnt)
    
    if board[bluey + dy][bluex + dx] == "O":
        falled = True

    return redx, redy, bluex, bluey, falled

# def printBoard():
#     [print(''.join(line)) for line in board]
#     print()
def find_shortest(redx:int, redy:int, bluex:int, bluey:int, cnt:int):
    global ans
    if cnt + 1 > 10: return


    for dx, dy in direct:
        nrx, nry, nbx, nby, isFalled = move(dx, dy, redx, redy, bluex, bluey, cnt + 1)
        
        if not isFalled:
            find_shortest(nrx, nry, nbx, nby, cnt + 1)

        board[nry][nrx] = "." ; board[redy][redx] = "R"
        board[nby][nbx] = "." ; board[bluey][bluex] = "B"

find_shortest(red_coor[0], red_coor[1], blue_coor[0], blue_coor[1], 0)

if ans > 10: ans = -1
print(ans)

