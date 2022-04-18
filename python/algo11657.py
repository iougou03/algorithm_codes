import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodeEdges = [[] for _ in range(n + 1)]
nodeWeight = [float("inf") for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    
    nodeEdges[a].append((c, b)) # (weight, end_point)


def edgeRelaxation():
    hadUpdate = False
    for node in range(1, n + 1):
        for nw, nn in nodeEdges[node]:
            if nodeWeight[node] == float("inf"): continue
            if nodeWeight[node] + nw < nodeWeight[nn]:
                nodeWeight[nn] = nodeWeight[node] + nw
                hadUpdate = True
    return hadUpdate

def bellmanFord(start):
    nodeWeight[start] = 0
    
    for _ in range(n - 1): edgeRelaxation()
    
    if edgeRelaxation(): return False
    else: return True

if bellmanFord(1):
    for ans in nodeWeight[2:]:
        if ans == float("inf"): print(-1)
        else: print(ans)
else:
    print(-1)
