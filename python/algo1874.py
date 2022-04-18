from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
num_queue = deque([i for i in range(1, n + 1)])
stack = []
input_queue = deque()
ans = []

for _ in range(n):
    input_queue.append(int(input()))

for itop in input_queue:
    if not stack:
        stack.append(num_queue.popleft())
        ans.append('+')
    stop = stack[-1]

    if num_queue:
        ntop = num_queue[0]
        
        while itop > stop:
            if ntop > itop:
                print("NO")
                sys.exit(0)
            stack.append(num_queue.popleft())
            ans.append('+')
            stop = stack[-1]

    if itop == stop:
        ans.append('-')
        stack.pop()
        continue
    
    if itop < stop:
        print("NO")
        sys.exit(0)

[print(a) for a in ans]