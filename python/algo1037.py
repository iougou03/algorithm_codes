import sys

t = int(sys.stdin.readline())
ans= 0
measure = list(map(int, sys.stdin.readline().split()))
min_val = sys.maxsize
max_val = 0

for val in measure:
    max_val = max(max_val, val)
    min_val = min(min_val, val)

ans = max_val * min_val

print(ans)