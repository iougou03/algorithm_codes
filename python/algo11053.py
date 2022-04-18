A = int(input())

seq = list(map(int, input().split()))
partial_max = [0 for _ in range(A + 1)]

# time complexity O(n^2)
# for i in range(A):
#     val = seq[i]
#     max_idx = 0
#     for j in range(i):
#         if val > seq[j]:
#             max_idx = max_idx if partial_max[j + 1] < partial_max[max_idx] else j + 1
#     partial_max[i + 1] = partial_max[max_idx] + 1

# print(max(partial_max))


# time complexity O(n log n)
partial_dynamic_max= [0]

def bsearch(val):
    global partial_dynamic_max
    left = 0 ; right = len(partial_dynamic_max) - 1
    
    while(left <= right):
        middle = (left + right) // 2
        if partial_dynamic_max[middle] > val: right = middle - 1
        elif partial_dynamic_max[middle] < val: left = middle + 1
        else: left = middle ; break

    if left < len(partial_dynamic_max):
        partial_dynamic_max[left] = min(partial_dynamic_max[left], val)
    else: 
        partial_dynamic_max.append(val)
    # return left

for i in range(A):
    val = seq[i]
    bsearch(val)
    # partial_max[i + 1] = max_val

print(len(partial_dynamic_max) - 1)
