from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nodeEdges=[[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
ans = 0

for _ in range(m):
    u, v = map(int ,input().split())
    nodeEdges[u].append(v)
    nodeEdges[v].append(u)

def bfs(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if visited[node]: continue
        visited[node] = 1

        for nextNode in nodeEdges[node]:
            if not visited[nextNode]:
                queue.append(nextNode)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        ans +=1

print(ans)