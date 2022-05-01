radixNum, radix = input().split()
radix = int(radix)

def translate(n):
    if ord("A") <= ord(n) <= ord("Z"):
        return ord(n) - ord("A") + 10
    else:
        return int(n)
top = len(radixNum) - 1 ; exp = 0
ans = 0

while top >= 0:
    ans += translate(radixNum[top]) * radix ** exp

    exp += 1 ; top -= 1

print(ans)