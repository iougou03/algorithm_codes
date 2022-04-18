import heapq, sys

input = sys.stdin.readline
n = int(input())
maxHeap = []
ans = []

for _ in range(n):
    val = int(input())
    if val == 0: 
        if maxHeap: ans.append(heapq.heappop(maxHeap)[1])
        else: ans.append(0)
    else: heapq.heappush(maxHeap, [-val,val])

[print(a) for a in ans]