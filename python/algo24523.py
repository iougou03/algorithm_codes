n = int(input())

arr = list(map(int, input().split()))
ans = []
cnt = 1

for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        cnt += 1
    else:
        for j in range(cnt):
            ans.append(i + 2)
        cnt = 1
if cnt:
    for i in range(cnt): ans.append(-1)

[print(a, end = " ") for a in ans]