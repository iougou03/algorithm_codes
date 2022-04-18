import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inputList = []

parent = [-1 for _ in range(n)]
rank = [0 for _ in range(n)]

def find(node):
    if parent[node] == -1:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        if rank[aRoot] > rank[bRoot]:
            parent[bRoot] = aRoot
        elif rank[aRoot] < rank[bRoot]:
            parent[aRoot] = bRoot
        else:
            parent[bRoot] = aRoot
            rank[aRoot] += 1
        return False
    else:
        return True

ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if ans: continue
    if union(a, b): ans = i + 1

print(ans)