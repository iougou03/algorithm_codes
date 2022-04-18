n = int(input())
ropes = []

for i in range(n):
    ropes.append(int(input()))

ropes.sort()
ans = 0

for i in range(n):
    ans = max(ropes[i] * (n - i), ans)

print(ans)