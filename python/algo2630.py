# 가로 세로 반씩 나눠보면서 하나의 색으로 이루어진 정사각형이 몇개 나오는가
N = int(input())
ans = {'1': 0, '0': 0}
squares = []

def solution(x, y, squareSize):
    first_col = squares[y][x]

    if squareSize != 1:
        for ny in range(y, y + squareSize):
            for nx in range(x, x + squareSize):
                if first_col != squares[ny][nx]:
                    squareSize //= 2
                    # 1
                    solution(x,y, squareSize)
                    # 2
                    solution(x + squareSize, y, squareSize)
                    # 3
                    solution(x, y + squareSize , squareSize)
                    # 4
                    solution(x + squareSize, y + squareSize, squareSize)
                    return
    
    ans[str(first_col)] += 1

for _ in range(N):
    squares.append(list(map(int, input().split())))
# x, y
solution(0, 0, N)

print(ans['0'])
print(ans['1'])
