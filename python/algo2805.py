n, m = map(int, input().split())
h_list = list(map(int, input().split()))

def check_valid(h,needHeight):
    cut = 0
    for treeHeight in h_list:
        cut += treeHeight - h if treeHeight - h >= 0 else 0
        if needHeight <= cut: return True
    return False

left = 0 ; right = 2000000000

while left <= right:
    middle = (left + right) // 2

    if check_valid(middle, m): left = middle + 1
    else: right = middle - 1
    
print(right)