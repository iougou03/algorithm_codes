from collections import deque

A, B, C = map(int , input().split())

ans = 0
visited = [[0] * 1501 for _ in range(1501)]

sumVal = A + B + C

if sumVal % 3 != 0:
    print(0)
else:
    queue = deque([[A, B]])
    visited[A][B] = 1

    while queue:
        g1, g2 = queue.popleft()

        temp = [g1, g2, sumVal - g2 - g1]

        for i in range(3):
            for j in range(3):
                if temp[i] < temp[j]:
                    v1 = temp[i] + temp[i]
                    v2 = temp[j] - temp[i]
                    if visited[v1][v2]: continue

                    visited[v1][v2] = 1
                    queue.append([v1, v2])

    print(visited[sumVal // 3][sumVal // 3])