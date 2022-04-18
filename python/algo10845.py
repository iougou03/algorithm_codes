from collections import deque
import sys
input = sys.stdin.readline

queue = deque()

def push(x): queue.append(x)
def pop(): return queue.popleft() if queue else -1
def size(): return len(queue)
def empty(): return 0 if queue else 1
def front(): return queue[0] if queue else -1
def back(): return queue[-1] if queue else -1

functions = {
    "push": push,
    "pop": pop,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back,
}

n = int(input())
ansList = []

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        functions[command[0]](command[1])
    else:
        ansList.append(functions[command[0]]())

[print(ans) for ans in ansList]