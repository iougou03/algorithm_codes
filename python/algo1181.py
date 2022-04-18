n = int(input())
arr = {}

for _ in range(n):
    word = input()
    arr[word] = len(word)

ans = []
for k, v in arr.items():
    ans.append([v, k])

ans.sort(key=lambda x:x[1])
ans.sort(key=lambda x:x[0])

[print(a[1]) for a in ans]