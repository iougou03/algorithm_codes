string = input()
ans = []

for i in range(len(string)):
    ans.append(string[i:])

ans.sort()

[print(a) for a in ans]