from collections import deque

n, k = map(int, input().split())
nums = deque([i for i in range(1, n + 2)])
# ans = [] ; cnt = 1

# while len(ans) < n:
#     if cnt < k: 
#         cnt += 1
#         nums.append(nums.popleft())
    
#     if cnt == k:
#         ans.append(nums.popleft())
#         cnt = 1

    
# print("<",end="")
# for a in ans[:-1]:
#     print(a,end=", ")
# print(ans[-1],end=">")