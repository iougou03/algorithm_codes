# def solution(idx, selected, set_s, k, end):
#     if len(selected) == end:
#         print(*selected)
#         return

#     for i in range(idx + 1, k):
#         solution(i, selected + [set_s[i]], set_s, k, end)

# while True:
#     case = list(map(int, input().split()))
#     if case[0] == 0: break

#     for i in range(case[0]):
#         solution(i, [case[i + 1]], case[1:], case[0], 6)
#     print()

# 2022-05-06
n = int(input())
seq = list(map(int, input().split()))

dp_per_length = [1001 for _ in range(n + 1)]
ans = 0

def check_num(num):
    global n
    idx = 1

    while idx < n:
        if num <= dp_per_length[idx]: 
            dp_per_length[idx] = num
            break
        idx += 1

    return idx
    
for num in seq:
    ans = max(ans, check_num(num))

print(ans)
