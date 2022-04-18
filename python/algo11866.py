# 1 2 3 4 5 6 7 
# 1 2 4 5 6 7
# 1 2 4 5 7
# 1 4 5 7
# 1 4 5
# 1 4
# 4
N , K = map(int, input().split())
ans = []
queue = [i for i in range(1, N + 1)]
idx = 0

while(queue):
    if len(queue) - 1 < idx + K - 1: idx = (idx + (K - 1)) % len(queue)
    else: idx += K - 1
    
    ans.append(queue[idx]) ; del queue[idx]
    if len(queue) - 1 < idx: idx = 0

print("<", end="")
if len(ans) <= 1: print(ans[0], end="")
else:
    for i in range(len(ans) - 1):
        print(ans[i],end=", ")
    print(ans[len(ans) - 1],end="")
print(">", end="")
