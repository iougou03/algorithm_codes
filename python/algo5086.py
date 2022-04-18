ans = []

while 1:
    a,b = map(int, input().split())
    if a == 0 or b == 0: break

    if b % a == 0: ans.append("factor")
    elif a % b == 0: ans.append("multiple")
    else: ans.append("neither")

[print(a) for a in ans]