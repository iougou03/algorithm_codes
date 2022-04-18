import heapq, sys

MAX_VAL = 3000001
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph=[[] for _ in range(v + 1)]
w_list = [MAX_VAL] * (v + 1)
w_list[k] = 0
heap = []

for _ in range(e):
    x, y, weight = map(int, input().split())
    graph[x].append((y, weight))

def dijkstar(start):
    heapq.heappush(heap ,(start,0))

    while heap:
        node, weight = heapq.heappop(heap)
        
        if w_list[node] < weight: continue

        for neighbor, nei_weight in graph[node]:
            next_weight = weight + nei_weight
            if w_list[neighbor] > next_weight:
                w_list[neighbor] = next_weight
                heapq.heappush(heap, (neighbor, next_weight))
# dijkstar(k)

# for w in w_list[1:]:
#     if w == MAX_VAL: print("INF")
#     else: print(w)

# import heapq
# import sys

# input = sys.stdin.readline
# MAX_VAL=sys.maxsize

# v, e = map(int, input().split())
# k = int(input())
# w_list = [MAX_VAL] *(v + 1)
# heap =[]
# graph=[[] for _ in range(v + 1)]

# def dijkstar(start):
#     w_list[start] = 0
#     heapq.heappush(heap, (0, start)) 
    
#     while heap:
#         weight, node = heapq.heappop(heap)
        
#         if w_list[node] < weight: 
#             continue

#         for neighbor, dw in graph[node]:
#             nw = dw + weight
#             if nw < w_list[neighbor]:
#                 w_list[neighbor] = nw
#                 heapq.heappush(heap, (nw, neighbor))

# for _ in range(e):
#     x, y, weight = map(int, input().split())
#     graph[x].append((y, weight))

# dijkstar(k)
# for i in range(1,v+1):
#     print("INF" if w_list[i]== MAX_VAL else w_list[i])


import heapq
import sys

input = sys.stdin.readline
MAX_VAL=3000001

v, e = map(int, input().split())
k = int(input())

graph=[[] for _ in range(v + 1)]
w_list = [MAX_VAL] *(v + 1)
w_list[k] = 0

def dijkstar(start):
    heap = [(0,start)]

    while heap:
        weight, node = heapq.heappop(heap)
        
        if w_list[node] < weight: continue

        for nei_weight, neighbor in graph[node]:
            next_weight = weight + nei_weight
            if w_list[neighbor] > next_weight:
                w_list[neighbor] = next_weight
                heapq.heappush(heap, (next_weight, neighbor))

for _ in range(e):
    x, y, weight = map(int, input().split())
    graph[x].append([weight, y])

dijkstar(k)

for i in range(1,v+1):
    if w_list[i]== MAX_VAL: print("INF")
    else: print(w_list[i])