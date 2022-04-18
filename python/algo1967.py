import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int,input().split())
    tree[a].append((w, b))
    tree[b].append((w, a))


def dfs(start):
    stack = [(0, start)]
    visited = [0 for _ in range(n + 1)]
    cnt = 0 ; farthestNode = 0

    while stack:
        length, node = stack.pop()
        visited[node] = 1
        if cnt < length:
            farthestNode = node  
            cnt = length

        for nw, nn in tree[node]:
            if not visited[nn]:
                stack.append((length + nw, nn))

    return (farthestNode, cnt)

print(dfs(dfs(1)[0])[1])


# ------------------------------------------------------------------

# my version
# ans = 0
# def searchTreeWidth(node):
#     global ans
#     maxLength = 0

#     if tree[node].childs:
#         childList = []
#         for i in range(len(tree[node].childs)):
#             childNode = tree[node].childs[i]
#             sumLength = searchTreeWidth(childNode) + tree[node].childsWeight[i]
            
#             childList.append(sumLength)

#         childList.sort(reverse=True)

#         maxLength = childList[0]

#         dp[node] = maxLength

#         if len(childList) > 1: 
#             dp[node] += childList[1]
    
#     ans = max(ans ,dp[node])
#     return maxLength
    
# searchTreeWidth(1)

# print(ans)