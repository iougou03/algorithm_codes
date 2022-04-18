n = int(input())

numList = list(map(int, input().split()))
numList.sort()

m = int(input())
findList = list(map(int, input().split()))

def bsearch(num):
    global n
    left = 0 ; right = n - 1

    while left <= right:
        middle = (left + right) // 2

        if numList[middle] < num: left = middle + 1
        elif numList[middle] == num: return 1
        else: right = middle - 1
    
    if numList[left - 1] == num: return 1
    else: return 0

for fn in findList:
    print(bsearch(fn))