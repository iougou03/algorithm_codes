n = int(input())
radius = list(map(int, input().split()))

def get_gcd(a, b):
    if a < b: a, b = b, a
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a

numer = 1 ; deno = 1
for i in range(len(radius) - 1):
    numer *= radius[i]
    deno *= radius[i + 1]
    gcd = get_gcd(numer, deno)
    numer //= gcd ; deno //= gcd
    print(f"{numer}/{deno}")