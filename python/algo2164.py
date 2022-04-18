# from collections import deque

# n = int(input())
# num_list = deque([i + 1 for i in range(n)])

# while len(num_list) != 1:
#     print(num_list)
#     num_list.popleft()
#     if len(num_list) == 1:
#         break
#     num_list.append(num_list.popleft())

# print(num_list[0])



n = int(input())
top = 0
num_list = [i + 1 for i in range(n)]

while top < n:
    print(num_list)
    top += 1
    if top >= n: break
    num_list[-1], num_list[top] = num_list[top], num_list[-1]

print(num_list[-1])