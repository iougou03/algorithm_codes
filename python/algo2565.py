n = int(input())

# version 2 - dp
poleList = []
dp = [[0,0] for _ in range(n + 1)]

for _ in range(n):
    x, y = map(int,input().split())
    poleList.append([x,y])

poleList.sort(key=lambda x: x[0])
ans = 0

for i in range(1, n + 1):
    dp[i][1] = poleList[i - 1][1]
    for j in range(i - 1, -1, -1):
        if dp[i][1] > dp[j][1]:
            dp[i][0] = max(dp[i][0], dp[j][0])
    dp[i][0] += 1
    ans = max(dp[i][0], ans)

print(n - ans)



# version 1
# poleAList = []
# dupList = [0 for _ in range(501)]

# for _ in range(n):
#     x, y = map(int,input().split())
#     poleAList.append([x, y])

# for a, b in poleAList:
#     for na, nb in poleAList:
#         if na == a: continue
        
#         if na < a and nb > b:
#             dupList[a] += 1
#         elif na > a and nb < b:
#             dupList[a] += 1

# poleAList = sorted(poleAList, key= lambda x: dupList[x[0]], reverse=True)
# ans = 0

# def check_empty():
#     status = True
#     for t in dupList:    
#         if t > 0: status = False
#     return status
# for a, b in poleAList:
#     print(dupList[1:11])
#     if check_empty(): break

#     dupList[a] = 0
#     for na, nb in poleAList:
#         if na == a: continue
        
#         if na < a and nb > b:
#             dupList[na] -= 1
#         elif na > a and nb < b:
#             dupList[na] -= 1
#     ans += 1

# print(ans)
