import sys
input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))
seqCnt = [0 for _ in range(1000001)]
stack = []
ansList = []

for i in range(n):
    seqCnt[seq[i]] += 1

for _ in range(n):
    cnt = seqCnt[seq[-1]]
    ans = -1
    if not stack: pass
    elif cnt < seqCnt[stack[-1]]:
        ans = stack[-1]
    else:
        while stack:
            if seqCnt[stack[-1]] > cnt:
                ans = stack[-1]
                break
            stack.pop()

    stack.append(seq.pop())
    ansList.append(ans)

print(*ansList[::-1])

