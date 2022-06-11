n = int(input())

edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())

    edges[x].append(y)
    edges[y].append(x)

bfs_str = list(map(int, input().split()))

def check_bfs_valid(bfs_str):
    global n
    pidx = 0 ; cidx = 1
# 1. 큐에 시작 정점을 넣는다. 이 문제에서 시작 정점은 1이다. 1을 방문했다고 처리한다 <-- I missed this statement :(
    if bfs_str[pidx] != 1: return False

    while pidx < n:
        parent_node = bfs_str[pidx]

        while cidx < n and bfs_str[cidx] in edges[parent_node]:
            cidx += 1
        
        pidx += 1
    
    if pidx == cidx: return True
    return False

if check_bfs_valid(bfs_str): print(1)
else: print(0)