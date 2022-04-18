from collections import deque

n, m = map(int, input().split())
num_list = deque([i + 1 for i in range(n)])
find_list = list(map(int, input().split()))

def move_left(): num_list.append(num_list.popleft())
def move_right(): num_list.appendleft(num_list.pop())
def pop(): num_list.popleft()

ans = 0

for fn in find_list:
    idx = num_list.index(fn)
    if idx < len(num_list) - idx:
        while True:
            if num_list[0] == fn: 
                pop()
                break
            ans += 1
            move_left()
    else:
        while True:
            if num_list[0] == fn: 
                pop()
                break
            ans += 1
            move_right()

print(ans)