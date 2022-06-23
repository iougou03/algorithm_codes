dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

ans = []
def brute(start, weight, dlist):
    global ans
    if len(dlist) == 7 and weight == 100:
        ans = dlist
        return
    
    if weight > 100 or start + 1 == 9: return

    for i in range(start + 1, 9):
        brute(i, weight + dwarfs[i], dlist + [dwarfs[i]])

for i in range(9):
    brute(i, dwarfs[i], [dwarfs[i]])


[print(a) for a in sorted(ans)]