n, s = map(int , input().split())

seq = list(map(int , input().split()))

top = 0 ; bottom = 0
sum = 0
ans = 100001

while top <= bottom and bottom < n:
    if sum < s:
        sum += seq[bottom]
        bottom += 1

    while sum >= s:
        ans = min(ans, bottom - top)
        sum -= seq[top]
        top += 1


if ans >= 100001: print(0)
else: print(ans)