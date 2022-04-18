import heapq
import sys

N = int(sys.stdin.readline())
heap = [] ; ans = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0: 
        if heap: ans.append(heapq.heappop(heap)[1])
        else: ans.append(0)
    else: heapq.heappush(heap,[abs(num), num])

[print(a) for a in ans]