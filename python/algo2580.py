# sudoku = []
# sudoku_check = []

# for i in range(9):
#     sudoku.append(list(map(int, input().split())))
#     sudoku_check.append([0 for _ in range(9)])
#     for j in range(9):
#         if sudoku[i][j] != 0: sudoku_check[i][sudoku[i][j] - 1] = 1

# # [print(row) for row in sudoku]

# for i in range(9):
#     if sudoku_check[i].count(0) == 1:
#         sudoku[i][sudoku[i].index(0)] = sudoku_check[i].index(0) + 1

# # for i in range(9):
# #     cnt = 0 ; position={}
# #     for j in range(9):
# #         sudoku_check
# [print(row) for row in sudoku_check]


# version 2.
import sys

sdoku = [] ; blanks = []

def solution(val, level):
    if level == len(blanks):
        for line in sdoku:
            [print(s, end=" ") for s in line]
            print()
        sys.exit(0) 
    
    cx, cy = blanks[level]
    row_valid = True ; col_valid = True ; square_valid = True

    for i in range(9):
        if i != cx and val == sdoku[cy][i]:
            row_valid = False
            break
        if i != cy and val == sdoku[i][cx]:
            col_valid = False
            break

    if not row_valid or not col_valid: return

    starty = cy // 3 * 3 ; startx = cx // 3 * 3
    for i in range(starty, starty + 3):
        for j in range(startx, startx + 3):
            if i == cy and j == cx: continue
            if val == sdoku[i][j]:
                square_valid = False
                break

    if square_valid:
        for i in range(1,10):
            sdoku[cy][cx] = val
            solution(i,level + 1)
            sdoku[cy][cx] = 0
    else: return

for y in range(9):
    sdoku.append(list(map(int, sys.stdin.readline().split())))
    for x in range(9):
        if sdoku[y][x] == 0: blanks.append([x,y])

for i in range(1,10):
    solution(i,0)

