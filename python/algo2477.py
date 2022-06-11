k = int(input())

d = [{} for _ in range(6)]
ds = [0, 0, 0, 0]

for i in range(6):
    di, le = map(int, input().split())

    d[i] = {
        'direction': di,
        'length': le,
    }
    ds[di - 1] += 1

sq1 = 1 ; sq2 = 1

didx1 = ds.index(1)
if ds[i] == 1:
    for j in range(6):
        if d[j]['direction'] == i + 1:
            sq1 *= d[j]['length']
    else:

