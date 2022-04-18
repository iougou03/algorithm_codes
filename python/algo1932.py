import sys
pyramid = []

N = int(sys.stdin.readline())

for _ in range(N):
    pyramid.append(list(map(int, sys.stdin.readline().split())))

def solution():
    global ans
    for i in range(1, N):
        for j in range(i + 1):
            left_child = j - 1 if j > 0 else -1
            right_child = j if j <= i - 1 else -1
            if left_child == -1: pyramid[i][j] += pyramid[i - 1][right_child]
            elif right_child == -1: pyramid[i][j] += pyramid[i - 1][left_child]
            else: pyramid[i][j] += max(pyramid[i - 1][left_child], pyramid[i - 1][right_child])

            ans = max(ans, pyramid[i][j])

ans = pyramid[0][0]
solution()
print(ans)