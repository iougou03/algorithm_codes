from collections import deque
import sys

T = int(sys.stdin.readline())

def solution(commands,arr):
    start_idx = 0 ; end_idx = len(arr) ; reverse= False ; c_idx = 0
    while(start_idx <= end_idx and c_idx < len(commands)):
        c = commands[c_idx]
        if c == "R": reverse = not reverse
        elif c == "D":
            if reverse: end_idx -= 1
            else: start_idx += 1
        c_idx += 1

    if start_idx > end_idx: return "error"
    ans = list(arr)[start_idx : end_idx]
    if reverse: ans.reverse()
    return "[" + ",".join(ans) + "]"

ans = []
for _ in range(T):
    p = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline()[1:-2].split(","))
    if arr[0] == '': arr = deque([])
    ans.append(solution(p, arr))

[print(a) for a in ans]