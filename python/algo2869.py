n = int(input())
ans = 0

def nQueen(xIdx, xPerLevel, yIdx):
    global ans
    xPerLevel.append(xIdx) ; yIdx += 1

    for nx in range(n):
        isPossible = True
        for level in range(yIdx):
            if nx == xPerLevel[level]: 
                isPossible = False
                break
            gx = abs(nx - xPerLevel[level]) ; gy = abs(yIdx + 1 - level)


for i in range(n):
    nQueen(i, [], -1)

print(ans)
