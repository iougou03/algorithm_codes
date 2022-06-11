import random, bisect, time

a = [int(random.random() * 100) for _ in range(10000000)]


search = a[int(random.random() * 10000000)]

a.sort()

start = time.time()
left = 0 ; right = len(a) - 1

while left <= right:
    middle = (left + right) // 2

    if a[middle] < search: left = middle + 1
    else: right = middle - 1

print(f"--------------\nfind number! idx : {left}\n--------------")
print(time.time() - start)

start = time.time()
l = bisect.bisect_left(a, search)
print(f"--------------\nfind number! idx : {l}\n--------------")
print(time.time() - start)
