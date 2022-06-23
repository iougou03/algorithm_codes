from collections import deque

n = int(input())

board = [list(input()) for _ in range(n)]
ans = 0


def brute(x1, y1, x2, y2, n):
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]
    initColor = board[y1][x1]
    column = 0 ; row = 0

    left = y1
    while left >= 0 and board[left][x1] == initColor:
        column += 1
        left -= 1

    left = x1
    while left >= 0 and board[y1][left] == initColor:
        row += 1
        left -= 1

    right = y1 + 1
    while right < n and board[right][x1] == initColor:
        column += 1
        right += 1

    right = x1 + 1
    while right < n and board[y1][right] == initColor:
        row += 1
        right += 1
    
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]

    return max(row, column)

def check_valid(x, y, n):
    if x >= n or y >= n or x < 0 or y < 0: return False

    return True

for y in range(n):
    for x in range(n):
        v1 = 0 ; v2 = 0 ; v3 = 0 ; v4 = 0
        if not check_valid(x, y, n): continue
        if check_valid(x, y + 1, n): v1 = brute(x, y, x, y + 1, n)
        if check_valid(x, y - 1, n): v2 = brute(x, y, x, y - 1, n)
        if check_valid(x + 1, y, n): v3 = brute(x, y, x + 1, y, n)
        if check_valid(x - 1, y, n): v4 = brute(x, y, x - 1, y, n)

        ans = max([v1, v2, v3, v4, ans])

print (ans)