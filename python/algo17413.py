from collections import deque

string = input()
string += " "

stack = [] ; queue = deque()
ans = ""

for char in string:
    if char == "<":
        queue.append(char)

        while stack: ans += stack.pop()

    elif char == ">":
        queue.append(char)

        ans += "".join(queue)
        queue = []
    elif stack and char == " ":
        while stack: ans += stack.pop()
        ans += " "
    else:
        if queue: queue.append(char)
        else: stack.append(char)

print(ans)