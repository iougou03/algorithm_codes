# import sys
# input = sys.stdin.readline

# v, e = map(int, input().split())
# # graph = [[float("inf") for _ in range(v + 1)] for _ in range(v + 1)]
# # before = [[float("inf") for _ in range(v + 1)] for _ in range(v + 1)]

# # def floyd_warshall():
# #     global v
# #     for mid in range(1, v + 1):
# #         for start in range(1, v + 1):
# #             for end in range(1, v + 1):
# #                 if graph[start][end] > graph[start][mid] + graph[mid][end]:
# #                     graph[start][end] = graph[start][mid] + graph[mid][end]
# #                     before[start][end] = before[mid][end]

# # for _ in range(e):
# #     a, b, c = map(int, input().split())
# #     graph[a][b] = c

# # floyd_warshall()

# # ans = float("inf")

# # for start in range(1, v + 1):
# #     for end in range(1, v + 1):
# #         if start == end: continue
# #         if graph[start][end] != float("inf") and graph[end][start] != float("inf"):
# #             ans = min(graph[start][end] + graph[end][start] , ans)

# # if ans != float("inf"): print(ans)
# # else: print(-1)

n = int(input())

for _ in range(n):
    words = list(input().split())
    for w in words:
        w = list(w)
        w.reverse()
        print("".join(w), end=" ")
    print()
    