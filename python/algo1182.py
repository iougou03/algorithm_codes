N, S = map(int, input().split())
seq = list(map(int, input().split()))
visited = [0 for _ in range(N)]
ans = 0

def solution(level, node, val):
    global N, S, ans
    if level > -1 and val == S: ans += 1

    if level == N - 1: return

    for i in range(node, N):
        if i != node and not visited[i]:
            visited[i] = 1
            solution(level + 1, i, val + seq[i])
            visited[i] = 0

solution(-1, -1, 0)
print(ans)