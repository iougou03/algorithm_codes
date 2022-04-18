from collections import deque

n = int(input())
stack = deque([])
ans = []

def push(x):
    stack.append(x)

def pop():
    if not stack: x = -1
    else: x = stack.pop()
    return x

def size():
    return len(stack)

def empty():
    x = 0
    if not stack: x = 1
    return x

def top():
    if stack: x = stack[-1]
    else: x = -1 
    return x

functions = {
    "push": push,
    "pop": pop,
    "size": size,
    "empty": empty,
    "top": top,
}

for i in range(n):
    command = input().split()
    if len(command) == 1: ans.append(functions[command[0]]())
    else: functions[command[0]](command[1])

[print(a) for a in ans]
