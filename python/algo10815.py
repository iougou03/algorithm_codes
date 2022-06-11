n = int(input())
nseq = list(map(int, input().split()))

m = int(input())
mseq = list(map(int, input().split()))

nseq.sort()

def bsearch(num):
    global n
    left = 0 ; right = n - 1

    while left <= right:
        middle = (left + right) // 2

        if nseq[middle] < num: left = middle + 1
        elif nseq[middle] == num: return True
        else: right = middle - 1
    
    if nseq[left - 1] == num: return True
    else: return False

for num in mseq:
    if bsearch(num): print(1, end=" ")
    else: print(0, end=" ")
