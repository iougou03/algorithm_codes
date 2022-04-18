import sys
input = sys.stdin.readline

n = int(input())
numList = []
for _ in range(n):
    numList.append(int(input()))

def getGcd(a, b):
    if a < b: a, b = b, a
    
    while b != 0:
        mod = a % b
        a = b
        b = mod
    
    return a

def getDivisor(num):
    d = int(num ** 0.5)
    divList = []

    while d > 1:
        if num % d == 0:
            if num // d == d: 
                divList.append(d)
            else:
                divList.append(d)
                divList.append(num // d)
        d -= 1

    return divList

num1 = abs(numList[0] - numList[1])
for i in range(1, n - 1):
    num2 = abs(numList[i] - numList[i + 1])
    gcd = getGcd(num1, num2)
    num1 = gcd

ans = [num1] + getDivisor(num1)

[print(a) for a in sorted(ans)]

# ansList = set()
# for i in range(n):
#     for j in range(i + 1, n):
#         if i == j: continue
#         gap1 = abs(numList[i] - numList[j])
#         gap2 = numList[i] % numList[j] if numList[i] > numList[j] else numList[j] % numList[i]
#         mod1 = numList[i] % gap1
#         mod2 = numList[i] % gap2
        
#         status1 = True ; status2 = True
#         for k in range(n):
#             if mod1 != numList[k] % gap1: status1 = False
#             if mod2 != numList[k] % gap2: status2 = False
            
#             if not status1 and not status2: break
#         if status1: ansList.add(gap1)
#         if status2: ansList.add(gap2)
    
# [print(a, end=" ") for a in ansList]