MAX_NUM = 2000000
numSetList = [0 for _ in range(MAX_NUM + 1)]

n = int(input())
numList = list(map(int, input().split()))
x = int(input())

for num in numList:
    if num < x:
        numSetList[num] = 1

ans = 0
half = x // 2 if x % 2 == 0 else x // 2 + 1
for i in range(1, half):
    if numSetList[i] and numSetList[x - i]:
        ans += 1

print(ans)