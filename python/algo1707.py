from collections import deque
import sys

k = int(sys.stdin.readline())

def bfs_check(start, visited):
    queue = deque([[start, start]])
    
    while queue:
        node, prev = queue.popleft()
        if visited[node]: continue
        visited[node] = 2 if visited[prev] == 1 else 1
        
        for neighbor in graph[node]:
            if visited[neighbor] == visited[node]: return False
            if not visited[neighbor]: queue.append([neighbor, node])
        
    return True

ans_list = []
for _ in range(k):
    ans = "YES"
    v, e = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(v)]
    visited = [0 for _ in range(v)]

    for __ in range(e):
        node1, node2 = map(int,sys.stdin.readline().split())
        graph[node1 - 1].append(node2 - 1)
        graph[node2 - 1].append(node1 - 1)

    for i in range(v): 
        if not visited[i]: 
            if not bfs_check(i, visited): 
                ans = "NO"
                break
    ans_list.append(ans)

[print(ans) for ans in ans_list]