# import heapq, sys

# input = sys.stdin.readline
# MAX_VAL = 200000000

# N, E = map(int, input().split())
# nodesEdges = [[] for _ in range(N + 1)]
# nodesWeight = [MAX_VAL for _ in range(N + 1)]

# for _ in range(E):
#     a, b, w = map(int, input().split())
#     nodesEdges[a].append([w, b])
#     nodesEdges[b].append([w, a])

# v1, v2 = map(int, input().split())

# def emptyNodes(): 
#     global nodesWeight
#     nodesWeight = [MAX_VAL for _ in range(N + 1)]

# def dijkstra(start):
#     heap = [(0, start)]
    
#     while heap:
#         weight, node = heapq.heappop(heap)
        
#         if nodesWeight[node]< weight: continue
#         nodesWeight[node] = weight

#         for nw, nn in nodesEdges[node]:
#             val = nw + weight
#             if nodesWeight[nn] > val: heapq.heappush(heap, (val , nn))

# dijkstra(1)
# ans1 = nodesWeight[v1] if nodesWeight[v1] != MAX_VAL else -1
# ans2 = nodesWeight[v2] if nodesWeight[v2] != MAX_VAL else -1
# emptyNodes()

# dijkstra(v1)
# if ans1 != -1: ans1 += nodesWeight[v2]
# if ans2 != -1: ans2 += nodesWeight[v2] + nodesWeight[N]
# emptyNodes()

# dijkstra(v2)
# if ans1 != -1: ans1 += nodesWeight[N]
# emptyNodes()

# if ans1 == -1 or ans2 == -1: print(-1)
# else: print(min(ans1, ans2))

# -----------------------------------------------------------------

import sys, heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def emptyDp():
    return [float("inf") for _ in range(n + 1)]


def dijkstra(start):
    heap = [(0, start)]

    while heap:
        weight, node = heapq.heappop(heap)
        if weight > dp[node]: continue
        dp[node] = weight

        for nw, nn in graph[node]:
            temp = nw + weight
            if dp[nn] > temp:
                heapq.heappush(heap, (temp, nn))

v1, v2 = map(int, input().split())

dp = emptyDp()
dijkstra(1)
if dp[v2] == float("inf") or dp[v1] == float("inf") or dp[n] == float("inf"):
    print(-1)
    sys.exit(0)

v1tov2 = dp[v1]
v2tov1 = dp[v2]

dp = emptyDp()
dijkstra(v1)
v1tov2 += dp[v2]
v2tov1 += dp[v2] + dp[n]

dp = emptyDp()
dijkstra(v2)
v1tov2 += dp[n]

print(min(v1tov2,v2tov1))
        