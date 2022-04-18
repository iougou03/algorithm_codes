from collections import deque
import sys
input = sys.stdin.readline
MAX_NUM = float("inf")

def dijkstra(start):
    queue = deque([start])
    nodesWeight = [MAX_NUM for _ in range(n + 1)]
    nodesWeight[start] = 0 

    while queue:
        node = queue.popleft()
        weight = nodesWeight[node]

        for nw, nn in roadsGraph[node]:
            temp = nw + weight
            if temp < nodesWeight[nn]:
                nodesWeight[nn] = temp
                queue.append(nn)

    return nodesWeight

t = int(input())

ansList = []
for _ in range(t):
    n, m, t = map(int, input().split())

    s, g, h = map(int, input().split())

    roadsGraph = [[] for _ in range(n + 1)]
    candiList = []
    gh = 0

    for _ in range(m):
        a, b, weight = map(int, input().split())
        roadsGraph[a].append((weight, b))
        roadsGraph[b].append((weight, a))
        if (a == g and b == h) or (a == h and b == g): gh = weight

    for _ in range(t): candiList.append(int(input()))

    sNodeWeight = dijkstra(s)
    closeNode = 0 ; farNode = 0

    if sNodeWeight[g] < sNodeWeight[h]:
        closeNode = g
        farNode = h
    else:
        closeNode = h
        farNode = g

    farNodeWeight = dijkstra(farNode)
    
    ans = []
    for cand in candiList:
        if sNodeWeight[cand] == MAX_NUM: continue
        if sNodeWeight[cand] == (sNodeWeight[closeNode] + gh + farNodeWeight[cand]):
            ans.append(cand)
    ans.sort()
    ansList.append(ans)

[print(*a) for a in ansList]