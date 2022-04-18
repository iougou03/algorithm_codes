t = int(input())
ans = []

def get_gcd(x,y):
    if x < y: x, y = y , x
    while y > 0:
        n = x % y
        x = y
        y = n
    return x

def get_lcm(x,y, gcd):
    return x * y // gcd

for _ in range(t):
    a, b = map(int, input().split())
    ans.append(get_lcm(a,b, get_gcd(a,b)))

[print(a) for a in ans]