dp = [[False for _ in range(31)] for _ in range(40001)]

v = int(input())
weightList = list(map(int, input().split()))

m = int(input())
marbleList = list(map(int, input().split()))

for w in weightList: dp[w][1] = True

for weight in range(1, 40001):
    for i in range(1, v):
        wi = weightList[i]

        
        if dp[abs(weight - wi)][i - 1]:
            dp[weight][i] = True
                
        



print(dp[:15])
    
# for m in marbleList:
#     state = False
#     for w in weightList:
#         if abs(m - w) != w and dp[abs(m - w)]:
#             state = True
#             break
#     if state: print("Y", end=" ")
#     else: print("N", end=" ")
