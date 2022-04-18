import sys

N = int(sys.stdin.readline())
stairs = [] ; points = [0 for _ in range(N)]

for i in range(N): 
    stairs.append(int(sys.stdin.readline()))

points[0] = stairs[0]
if N > 1:
    points[1] = stairs[0] + stairs[1]
if N > 2:
    points[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

    for i in range(3, N):
        points[i] = max(points[i - 3] + stairs[i - 1] + stairs[i], points[i - 2] + stairs[i])

print(points[-1])