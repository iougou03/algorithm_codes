n = int(input())
cards_list = list(map(int, input().split()))

m = int(input())
sangkeun_cards_list = list(map(int, input().split()))

cards_list.sort()

def upbsearch(arr, find):
    left = 0 ; right = len(arr) - 1

    while left < right:
        middle = (left + right) // 2
        if arr[middle] <= find: left = middle + 1
        else: right = middle
    return right

def downbsearch(arr, find):
    left = 0 ; right = len(arr) - 1

    while left < right:
        middle = (left + right) // 2
        if arr[middle] < find: left = middle + 1
        else: right = middle
    return right
print(cards_list)
for fn in sangkeun_cards_list:
    ub = upbsearch(cards_list, fn)
    db = downbsearch(cards_list, fn)
    if ub == n - 1 and cards_list[n - 1] == fn: ub += 1
    print(ub - db, end= " ")