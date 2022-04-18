import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    inpuList = list(map(int, input().split()))
    node = inpuList[0]
    for j in range(1 ,len(inpuList) - 1, 2):
        dest = inpuList[j] ; weight = inpuList[j + 1]
        graph[node].append((weight, dest))

ans = 0 ; ansNode = 0
visited = [0 for _ in range(V + 1)]

def dfs(node, weight):
    if visited[node]: return
    global ans, ansNode
    if ans < weight:
        ans = weight
        ansNode = node

    visited[node] = 1

    for nw, nn in graph[node]:
        if not visited[nn]:
            dfs(nn, weight + nw)

dfs(1, 0)

ans = 0
visited = [0 for _ in range(V + 1)]

dfs(ansNode, 0)

print(ans)
