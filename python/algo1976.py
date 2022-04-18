import sys

n = int(input())
m = int(input())
cityUnionParent = [0 for _ in range(n + 1)]

def find(node):
    if cityUnionParent[node]: 
        return find(cityUnionParent[node])
    else:
        return node

def union(node1, node2):
    node1Root = find(node1)
    node2Root = find(node2)

    if node1Root != node2Root:
        cityUnionParent[node2Root] = node1Root

for i in range(1, n + 1):
    relations = list(map(int, input().split()))
    for j in range(n):
        otherNode = j + 1
        if otherNode == cityUnionParent[i]: continue
        if relations[j]:
            union(i, otherNode)

ans = "YES"
travelList = list(map(int, input().split()))
root = find(travelList[0])

for t in travelList[1:]:
    if root != find(t):
        ans = "NO"
        break

print(ans)


# bfs - 15 min
# from collections import deque

# n = int(input())
# m = int(input())
# cities = [[] for _ in range(n + 1)]
# visited = [0 for _ in range(n + 1)]

# for i in range(1, n + 1):
#     nodes = list(map(int, input().split()))
#     for j in range(n):
#         if nodes[j]: cities[i].append(j + 1)

# travelPlan = list(map(int, input().split()))

# queue = deque([travelPlan[0]])

# while queue:
#     node = queue.popleft()
#     if visited[node]: continue
#     visited[node] = 1

#     for nextNode in cities[node]:
#         if not visited[nextNode]:
#             queue.append(nextNode)

# ans = "YES"
# for t in travelPlan:
#     if not visited[t]:
#         ans = "NO"
#         break

# print(ans)