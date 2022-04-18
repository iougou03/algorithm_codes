import sys
input = sys.stdin.readline
n = int(input())
sys.setrecursionlimit(100001)

# class bNode:
#     def __init__(self) -> None:
#         self.left = 0
#         self.right = 0

# tree = [bNode() for _ in range(n + 1)]
inorder = list(map(int, input().split()))
inorderIdx = [0 for _ in range(n + 1)]
for i in range(n):
    inorderIdx[inorder[i]] = i
postorder = list(map(int, input().split()))

def solution(root, rootInIdx, rootPostIdx, subTreeWidth, leftEnd):
    # print(root, rootInIdx, rootPostIdx, subTreeWidth, leftEnd, end = "\n")
    print(root,end = " ")

    leftSubTreeLength = rootInIdx - leftEnd
    rightSubTreeLength = (subTreeWidth - 1) - leftSubTreeLength
    
    # left subtree part
    if leftSubTreeLength == 1:
        leftRoot = inorder[rootInIdx - 1]
        print(leftRoot, end=" ") 
    elif leftSubTreeLength == 0:
        leftRoot = 0
    else:
        leftRoot = postorder[rootPostIdx - rightSubTreeLength - 1]

    # if leftRoot:
    #     tree[root].left = leftRoot

    if leftSubTreeLength > 1:
        solution(leftRoot, inorderIdx[leftRoot] ,rootPostIdx - rightSubTreeLength - 1, leftSubTreeLength, leftEnd)
    
    # right subtree part
    if rightSubTreeLength == 1:
        rightRoot = inorder[rootInIdx + 1]
        print(rightRoot, end=" ")
    elif rightSubTreeLength == 0:
        rightRoot = 0
    else:
        rightRoot = postorder[rootPostIdx - 1]

    # if rightRoot:
    #     tree[root].right = rightRoot
    
    if rightSubTreeLength > 1:
        solution(rightRoot, inorderIdx[rightRoot] ,rootPostIdx - 1, rightSubTreeLength, rootInIdx + 1)


initRoot = postorder[-1]
solution(initRoot ,inorderIdx[initRoot], n - 1, n, 0)

# def preorder(node):
#     print(node, end = " ")
#     if tree[node].left:
#         preorder(tree[node].left)
#     if tree[node].right:
#         preorder(tree[node].right)
# print()    

# preorder(initRoot)