n = int(input())

nums = [1 for _ in range(n + 1)]

idx = 2
pnums = []
while idx < n + 1:
    if nums[idx]:
        for i in range(idx * 2, n + 1, idx):
            if not nums[i]: continue
            nums[i] = 0
        pnums.append(idx)

    idx += 1

start = 0 ; end = 1
ans = 0

if pnums:
    sum = pnums[start]

    print(pnums)
    while start < end and end <= len(pnums):
        print(start ,end, sum)
        if sum < n:
            sum += pnums[end]
            end += 1
        
        elif sum == n:
            ans += 1
            sum -= pnums[start]
            start += 1
        
        else:
            sum -= pnums[start]
            start += 1

print(ans)