N = int(input())

queue = [1,2,3]

idx = 3
while idx < N:
    queue.append((queue[-1] + queue[-2]) % 15746)
    idx += 1
    del queue[0]
if N < idx:
    print(queue[N - 1])
else:
    print(queue[-1]) 