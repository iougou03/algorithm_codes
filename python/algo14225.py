n = int(input())

seq = list(map(int, input().split()))

nums = [0 for _ in range(100000 * n + 1)]

def solution(start, val, end):
    nums[val] = 1

    for i in range(start + 1, end):
        solution(i, val + seq[i], end)

for i in range(n): solution(i, seq[i], n)

idx = 1
while nums[idx]: idx += 1

print(idx)