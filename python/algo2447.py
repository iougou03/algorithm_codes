n = int(input())
starList = [[" " for _ in range(n)] for _ in range(n)]

def printStar(startx, starty, length):
    if length == 1: 
        starList[starty][startx] = "*"
        return
    
    dl = length // 3
    printStar(startx, starty, dl)
    printStar(startx + dl, starty, dl)
    printStar(startx + dl * 2, starty, dl)
    
    printStar(startx, starty + dl, dl)
    printStar(startx + dl * 2, starty + dl, dl)

    printStar(startx, starty + dl * 2, dl)
    printStar(startx + dl, starty + dl * 2, dl)
    printStar(startx + dl * 2, starty + dl * 2, dl)

printStar(0, 0, n)

for star in starList:
    [print(s,end = "") for s in star]
    print()