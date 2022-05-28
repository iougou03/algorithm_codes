n, m = map(int, input().split())

seq = list(map(int, input().split()))

ans = 0
top = 0 ; bottom = 0

while bottom <= n:
    if sum(seq[top: bottom]) < m:
        bottom += 1
    elif sum(seq[top: bottom]) > m:
        top += 1
    else:
        ans += 1
        bottom += 1

print(ans)