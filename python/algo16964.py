n = int(input())
edges=[[] for _ in range(n + 1)]
positions = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int , input().split())
    
    edges[x].append(y)
    edges[y].append(x)

dfs_str = list(map(int, input().split()))

for i in range(n):
    positions[dfs_str[i]] = i

ans = []
def check_valid(node, cnt):
    global ans
    if visited[node]: return 
    
    visited[node] = 1
    ans.append(node)
    cnt += 1

    if edges[node]:
        edge_weight = []
        
        for next_node in edges[node]:
            if visited[next_node]: continue
            edge_weight.append([positions[next_node], next_node])
        
        edge_weight.sort()
        
        for _, next_node in edge_weight:
            check_valid(next_node, cnt)
    

if dfs_str[0] == 1:
    
    visited = [0 for _ in range(n + 1)]

    check_valid(1, 0)

    print(1 if ans == dfs_str else 0)
    
else: print(0)