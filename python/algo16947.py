n = int(input())

edges = [[] for _ in range(n + 1)]

for _ in range(n):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

def dfs(start):
    global n
    MAX_LENGTH = 3001
    queue = [[start, 0, 0]]
    visited = [0 for _ in range(n + 1)]
    length = [MAX_LENGTH for _ in range(n + 1)]

    while queue:
        node, parent, cnt = queue.pop()

        if visited[node]: continue
        visited[node] = 1

        for next_node in edges[node]:
            if not visited[next_node]:
                length[next_node] = min(length[next_node], cnt + 1)
                queue.append( [next_node, node, cnt + 1] )
            
            elif visited[next_node] and parent != next_node:
                if MAX_LENGTH == length[next_node]:
                    return 0
                else:
                    return length[next_node]

for i in range(1, n + 1):
    print(dfs(i), end =" ")