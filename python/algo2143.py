import bisect


T = int(input())

n = int(input())
nseq = list(map(int , input().split()))

m = int(input())
mseq = list(map(int , input().split()))

ans = 0

nmem = [] ; mmem = []

for i in range(n):
    nsumval = 0
    for j in range(i, n):
        nsumval += nseq[j]
        nmem.append(nsumval)

for i in range(m):
    msumval = 0
    for j in range(i, m):
        msumval += mseq[j]
        mmem.append(msumval)

if len(nmem) < len(mmem):
    arrLarge = mmem
    arrSmall = nmem
else:
    arrLarge = nmem
    arrSmall = mmem

ans = 0

arrLarge.sort()

def leftBinarySearch(arr, num):
    left = 0 ; right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] < num: left = middle + 1
        else: right = middle - 1
    
    return left

def rightBinarySearch(arr, num):
    left = 0 ; right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] <= num: left = middle + 1
        else: right = middle - 1
    
    return left

for num in arrSmall:
    l = leftBinarySearch(arrLarge, T - num)
    r = rightBinarySearch(arrLarge, T - num)

    ans += r - l

print(ans)