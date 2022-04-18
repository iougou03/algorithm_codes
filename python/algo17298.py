n = int(input())

seq = list(map(int, input().split()))

ans = [] ; stack = []
for i in range(n):
    nge = -1 ; seq_pop = 0
    if not stack: 
        nge = -1
    elif seq[-1] < stack[-1]:
        nge = stack[-1]
    else:
        while stack:
            if seq[-1] < stack[-1]:
                nge = stack[-1]
                break
            stack.pop()
        
    ans.append(nge)
    stack.append(seq.pop())

[print(a,end=" ") for a in ans[::-1]]