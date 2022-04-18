from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [0 for _ in range(n + 1)]
nodeEdges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    nodeEdges[x].append(y)
    nodeEdges[y].append(x)

queue = deque([[1, 1]])

while queue:
    parent, node = queue.popleft()
    if visited[node]: continue
    visited[node] = parent
    
    for nextNode in nodeEdges[node]:
        if not visited[nextNode]:
            queue.append([node, nextNode])

[print(p) for p in visited[2:]]