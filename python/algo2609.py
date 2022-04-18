a,b = map(int, input().split())
gcp = 0
a_original = a ; b_original = b
while 1:
    n = a % b
    if n == 0:
        gcp = b
        break
    a = b
    b = n

print(gcp)
print(a_original * b_original // gcp)