digit = int(input())
ans = ""

while digit:
    if digit % -2 == 0:
        ans += "0"
        digit //= -2
    else:
        ans += "1"
        digit = digit // -2 + 1

if ans: print(ans[::-1])
else: print(0)


