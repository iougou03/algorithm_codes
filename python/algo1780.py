import sys

N = int(sys.stdin.readline())
paper = []
ans = {
    "-1": 0,
    "0": 0,
    "1": 0
}

def solution(startx, starty, square_size):
    val = paper[starty][startx]
    
    if square_size != 1:
        for y in range(starty, starty + square_size):
            for x in range(startx, startx + square_size):
                if val != paper[y][x]:
                    square_size //= 3
                    solution(startx , starty, square_size)

                    solution(startx + square_size, starty, square_size)
                    solution(startx + square_size * 2, starty, square_size)

                    solution(startx, starty + square_size, square_size)
                    solution(startx, starty + square_size * 2, square_size)

                    solution(startx + square_size, starty + square_size, square_size)

                    solution(startx + square_size * 2, starty + square_size, square_size)
                    solution(startx + square_size, starty + square_size * 2, square_size)

                    solution(startx +square_size * 2, starty + square_size * 2, square_size)
                    return
    ans[str(val)] += 1
    return

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

solution(0,0,N)

[print(a) for a in ans.values()]