t = int(input())
ansList = []

for _ in range(t):
    a , b = map(int, input().split())
    initial = a % 10
    digitList = [initial]
    lastDigit = initial
    while True:
        lastDigit = lastDigit * a % 10
        if lastDigit != initial: digitList.append(lastDigit)
        else: break
    
    ans = digitList[b % len(digitList) - 1]
    if ans == 0: ansList.append(10)
    else: ansList.append(ans)

[print(a) for a in ansList]