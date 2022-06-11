n, w, h = map(int , input().split())

for _ in range(n):
    l = int(input())

    if l <= w or l <= h or l**2 <= w**2 + h**2:
        print('DA')
    else:
        print('NE')