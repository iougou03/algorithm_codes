t = int(input())

for _ in range(t):
    ans = 0
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())

    for _ in range(n):
        cx, cy, r = map(int, input().split())

        p1_to_c = (x1 - cx)**2 + (y1 - cy) ** 2
        p2_to_c = (x2 - cx)**2 + (y2 - cy) ** 2


        if p1_to_c <= r**2 and p2_to_c <= r**2: continue
        if p1_to_c <= r**2: ans += 1
        elif p2_to_c <= r**2 : ans += 1

    print(ans)