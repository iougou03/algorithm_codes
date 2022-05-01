n, s = map(int, input().split())

brothers = list(map(int, input().split()))

def get_gcd(a, b):
    if a < b: a,b = b,a

    while b > 1:
        temp = a % b
        a = b
        b = temp

    return a

gcd = abs(s - brothers[0])

for b in brothers[1:]:
    gcd = get_gcd(gcd, abs(s - b))



print(gcd)