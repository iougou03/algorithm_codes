def solution():
    ans = 1
    for v in clothes_dict.values():
        ans *= (v + 1)
    return ans - 1
t = int(input())

ans = []
for _ in range(t):
    clothes_dict = {}
    n = int(input())
    for __ in range(n):
        name, clothes = input().split()
        if clothes in clothes_dict: clothes_dict[clothes] += 1
        else: clothes_dict[clothes] = 1
    ans.append(solution())

[print(a) for a in ans]