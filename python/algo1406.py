# import sys
# input = sys.stdin.readline

# class LinkedNode:
#     def __init__(self, char) -> None:
#         char = char if char else ""
#         self.char = char
#         self.left = None
#         self.right = None

# sentense = input()[:-1]

# sentense = [LinkedNode(c) for c in sentense]

# for i in range(len(sentense)):
#     if i == 0:
#         sentense[i].right = sentense[i + 1]
#     elif i == len(sentense) - 1:
#         sentense[i].left = sentense[i - 1]
#     else:
#         sentense[i].left = sentense[i - 1]
#         sentense[i].right = sentense[i + 1]

# m = int(input())
# cursor = LinkedNode("")
# sentense[-1].right = cursor
# cursor.left = sentense[-1]

# for _ in range(m):
#     command = input().split()
#     if len(command) == 1:
#         if command[0] == "L":
#             if cursor.left: cursor = cursor.left
#         elif command[0] == "D":
#             if cursor.right: cursor = cursor.right
#         elif command[0] == "B":
#             if not cursor.left: continue
#             elif not cursor.left.left:
#                 cursor.left = None
#             else:
#                 left = cursor.left.left
#                 left.right = cursor
#                 cursor.left = left
            
#     else:
#         node = LinkedNode(command[1])
#         if not cursor.left:
#             cursor.left = node
#             node.right = cursor
#         else:
#             left = cursor.left
#             node.left = left
#             node.right = cursor
#             left.right = node
#             cursor.left = node

# while cursor.left: cursor = cursor.left

# while cursor.right:
#     print(cursor.char,end = "")
#     cursor = cursor.right


import sys
input = sys.stdin.readline

string = input()
m = int(input())

leftStack = list(string)[:-1]
rightStack = []

for _ in range(m):
    command = input().split()
    if command[0] == 'P':
        leftStack.append(command[1])
    elif command[0] =="L":
        if leftStack: rightStack.append(leftStack.pop())
    elif command[0] =="D":
        if rightStack: leftStack.append(rightStack.pop())
    elif command[0] =="B":
        if leftStack: leftStack.pop()

print(*leftStack, *rightStack[::-1], sep="")