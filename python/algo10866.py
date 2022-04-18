from collections import deque
import sys

input = sys.stdin.readline
dq = deque([])

def push_front(x): dq.appendleft(x)
def push_back(x): dq.append(x)
def pop_front(): return dq.popleft() if dq else -1
def pop_back(): return dq.pop() if dq else -1
def size(): return len(dq)
def empty(): return 0 if dq else 1
def front(): return dq[0] if dq else -1
def back(): return dq[-1] if dq else -1

n = int(input())
ans = []
function_dict = {
    "push_front" : push_front,
    "push_back" : push_back,
    "pop_front" : pop_front,
    "pop_back" : pop_back,
    "size" : size,
    "empty" : empty,
    "front" : front,
    "back" : back,
}

for _ in range(n):
    command = input().split()
    if command[0] == "push_front": push_front(command[1])
    elif command[0] == "push_back": push_back(command[1])
    elif command[0] == "pop_front": ans.append(pop_front())
    elif command[0] == "pop_back": ans.append(pop_back())
    elif command[0] == "size": ans.append(size())
    elif command[0] == "empty": ans.append(empty())
    elif command[0] == "front": ans.append(front())
    else : ans.append(back())

[print(a) for a in ans]