n = int(input())
ans = 0
for i in range(5, n + 1, 5):
    while i % 5 == 0:
        ans += 1
        i //= 5

print(ans)