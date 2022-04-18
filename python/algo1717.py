# import sys

# input = sys.stdin.readline

# def find(a, b):
#     aRoot = getRoot(a)
#     bRoot = getRoot(b)
    
#     return "YES" if aRoot == bRoot else "NO"

# def getRoot(node):
#     while True:
#         if arr[node] != -1: node = arr[node]
#         else: break
#     return node

# def union(a, b):
#     aRoot = getRoot(a)
#     bRoot = getRoot(b)

#     if aRoot != bRoot: arr[bRoot] = aRoot

# n, m = map(int, input().split())
# arr = [-1 for _ in range(n + 1)]
# ans = []

# for _ in range(m):
#     command, a, b = map(int, input().split())
#     if command: ans.append(find(a,b))
#     else: union(a,b)

# [print(a) for a in ans]


# vers2 - recursive version
import sys

input = sys.stdin.readline

def find(node):
    if arr[node] == -1:
        return node
    arr[node] = find(arr[node])
    return arr[node]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot: arr[bRoot] = aRoot

n, m = map(int, input().split())
arr = [-1 for _ in range(n + 1)]
ans = []

for _ in range(m):
    command, a, b = map(int, input().split())
    if command: ans.append("YES" if find(a) == find(b) else "NO")
    else: union(a,b)

[print(a) for a in ans]