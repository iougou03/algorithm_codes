n = int(input())
seq = list(map(int , input().split()))
operatorCnt = list(map(int , input().split()))

def operation(idx, a, b):
    if idx == 0: return a + b
    elif idx == 1: return a - b
    elif idx == 2: return a * b
    elif idx == 3:
        if a < 0: return -(-a // b)
        else: return a // b

maxAns = -1000000001
minAns = 1000000001

def solution(level, val):
    global n, maxAns, minAns
    if level == n: 
        maxAns = max(maxAns, val)
        minAns = min(minAns, val)
        return

    for i in range(4):
        if operatorCnt[i] > 0:
            operatorCnt[i] -= 1
            solution(level + 1, operation(i, val, seq[level]))
            operatorCnt[i] += 1

solution(1, seq[0])

print(maxAns)
print(minAns)