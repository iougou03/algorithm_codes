N = int(input())
matrix = [] ; ans = ""

def check_square(startx,starty,length):
    global ans
    val = matrix[starty][startx]
    
    for y in range(starty,starty + length):
        for x in range(startx,startx + length):
            if val != matrix[y][x]: 
                quad_tree(startx, starty, length)
                return
    ans += str(val)
    return 

def quad_tree(startx,starty,length):
    global ans
    length //= 2
    ans += "("
    check_square(startx, starty, length)
    check_square(startx + length, starty, length)
    check_square(startx, starty + length, length)
    check_square(startx + length, starty + length, length)
    ans += ")"

[matrix.append(list(map(int,list(input())))) for _ in range(N)]

check_square(0,0,N)

print(ans)
