import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    candiList = []

    for _ in range(n):
        resumePoint , interviewPoint = map(int, input().split())
        candiList.append((resumePoint, interviewPoint))
    
    candiList.sort(key= lambda x: x[0])
    minIP = candiList[0][1]
    ans = 1
    # [print(c) for c in candiList]
    for i in range(1, n):
        if candiList[i][1] < minIP:
            ans += 1
            minIP = candiList[i][1]
    
    print(ans)
    