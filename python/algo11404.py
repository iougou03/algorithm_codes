import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
busEdges = [[[float("inf"), 0] for _ in range(n + 1)] for _ in range(n + 1)]
dijkdp = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if busEdges[a][b][0] > c: 
        busEdges[a][b][0] = c
        busEdges[a][b][1] = b

def dijkstra(start):
    global n
    heap = [(0, start)]
    visited = [0 for _ in range(n + 1)]
    dijkdp[start][start] = 0

    while heap:
        weight, node = heapq.heappop(heap)
        visited[node] = 1

        for nextWeight, nextNode in busEdges[node]:
            if not nextNode: continue

            if not visited[nextNode] and dijkdp[start][nextNode] > weight + nextWeight:
                dijkdp[start][nextNode] = weight + nextWeight
                heapq.heappush(heap, (weight + nextWeight, nextNode))

for i in range(1, n + 1): dijkstra(i)

for dp in dijkdp[1:]:
    for d in dp[1:]:
        if d == float("inf"):
            print(0, end=" ")
        else:
            print(d, end=" ")
    print()