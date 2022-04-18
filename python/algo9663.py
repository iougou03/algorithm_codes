N = int(input())

ans = 0
locations = [-1 for _ in range(N)]

def check_valid(idx, level):
    for i in range(level):
        if idx == locations[i] or abs(locations[i] - idx) == level - i: return False
    
    return True
    

def nQueen(level):
    global ans
    if level == N: 
        ans +=1
        return

    for i in range(N):
        if check_valid(i, level):
            locations[level] = i
            nQueen(level + 1)

nQueen(0)

print(ans)