import sys
input = sys.stdin.readline

def locate(coor):
    y = ord(coor[0]) - ord('A') + 1
    x = int(coor[1])

    return [x, y]

def findComb(a, b):
    if a > b: a, b = b, a
    return True if combSet[a][b] else False

def addComb(a, b):
    if a > b: a, b = b, a
    combSet[a][b] = 1

def removeComb(a, b):
    if a > b: a, b = b, a
    combSet[a][b] = 0

def checkSudokuValid(x, y, val):
    if x > 9 or y > 9: return False

    if sudominokuGrid[y][x]: return False

    for i in range(1, 10):
        if sudominokuGrid[y][i] == val or sudominokuGrid[i][x] == val:
            return False

    for i in range(1, 4):
        for j in range(1, 4):
            if sudominokuGrid[3 * ((y - 1) // 3) + i][3 * ((x - 1) // 3) + j] == val:
                return False
    
    return True
    
def sudoku(x, y, cnt):
    global COMPLETE
    if sudominokuGrid[y][x]:
        if x + 1 < 10: sudoku(x + 1, y, cnt)
        elif y + 1 < 10: sudoku(1, y + 1, cnt)
        elif cnt == 36: COMPLETE = True
    else:
        for i in range(1, 10):
            if checkSudokuValid(x, y, i):
                sudominokuGrid[y][x] = i

                for j in range(1, 10):
                    if i == j: continue
                    
                    if checkSudokuValid(x + 1, y, j) and not findComb(i, j):
                        sudominokuGrid[y][x + 1] = j
                        addComb(i, j)
                        sudoku(x, y, cnt + 1)
                        if COMPLETE: return

                        removeComb(i, j)
                        sudominokuGrid[y][x + 1] = 0


                    if checkSudokuValid(x, y + 1, j) and not findComb(i, j):
                        sudominokuGrid[y + 1][x] = j
                        addComb(i, j)
                        sudoku(x, y, cnt + 1)
                        if COMPLETE: return

                        removeComb(i, j)
                        sudominokuGrid[y + 1][x] = 0


                sudominokuGrid[y][x] = 0

def printGrid(level):
    print(f'Puzzle {level}')
    [print(''.join(list(map(str, grid[1:])))) for grid in sudominokuGrid[1:]]

idx = 0
while True:
    t = int(input())
    if t == 0: break
    idx += 1

    COMPLETE = False

    sudominokuGrid = [[0]*10 for _ in range(10)]
    combSet = [[0]*10 for _ in range(10)]

    for _ in range(t):
        U, LU, V, LV = input().split()
        x1, y1 = locate(LU)
        sudominokuGrid[y1][x1] = int(U)
        x2, y2 = locate(LV)
        sudominokuGrid[y2][x2] = int(V)

        addComb(int(U), int(V))

    numCoors = input().split()

    for i in range(9):
        x, y = locate(numCoors[i])
        sudominokuGrid[y][x] = i + 1
    
    sudoku(1, 1, t)
    printGrid(idx)
