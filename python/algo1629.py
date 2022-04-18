import sys

A,B,C = map(int, sys.stdin.readline().split())
B_copy = B ; queue = []

while(B_copy > 0):
    if B_copy % 2 == 0: queue.append(False) #even
    else: queue.append(True) #odd
    B_copy //= 2

ans = A

for i in range(len(queue) - 2, -1, -1):
    ans = ans**2 % C
    if queue[i]: ans = ans * A % C

print(ans % C)