a, b = map(int, input().split())

def checkNum(num):
    d = num % 10
    if d % 2 == 0: return num // 2
    elif d == 1: return num // 10
    else: return -1

ans = 1
while a != b and b > 0:
    b = checkNum(b)
    if b == -1: break
    ans += 1

if b <= 0: print(-1)
else: print(ans)