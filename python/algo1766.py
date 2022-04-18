import heapq, sys

class Node:
    def __init__(self) -> None:
        self.degree = 0
        self.child = []
input = sys.stdin.readline

n, m = map(int, input().split())
nodeList = [Node() for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    nodeList[a].child.append(b)
    nodeList[b].degree += 1

heap = []
ans = []

for i in range(1, n + 1):
    if nodeList[i].degree == 0: heapq.heappush(heap, i)

while heap:
    node = heapq.heappop(heap)
    ans.append(node)

    for c in nodeList[node].child:
        nodeList[c].degree -= 1

        if nodeList[c].degree == 0:
            heapq.heappush(heap, c)

[print(a, end= " ") for a in ans]