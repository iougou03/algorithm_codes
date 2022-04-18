n, m = map(int, input().split())


def getNum(num, factNum):
    cnt = 0
    while factNum > 0:
        cnt+= factNum // num
        factNum //= num

    return cnt

if m != 0:
    cnt5 = getNum(5, n) - getNum(5, n - m) - getNum(5, m)
    cnt2 = getNum(2, n) - getNum(2, n - m) - getNum(2, m)
    print(min(cnt5, cnt2))
else:
    print(0)