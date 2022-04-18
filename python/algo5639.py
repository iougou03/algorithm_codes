import sys
sys.setrecursionlimit(11000)

input = sys.stdin.readline
cnt = 0
def postorder(start, end):
    global cnt
    cnt += 1
    if start >= end: 
        return

    if end - start == 1:
        print(preorder[start])
        return
    
    leftIdx = start + 1
    rightIdx = leftIdx

    for i in range(start + 1, end):
        if preorder[start] < preorder[i]:
            rightIdx = i
            break

    postorder(leftIdx, rightIdx)
    postorder(rightIdx, end)
    print(preorder[start])

preorder = []
idx = 0

while True:
    try:
        preorder.append(int(input()))
        idx += 1
    except Exception:
        postorder(0, idx)
        break
