string = input()
stack = [string[0]]
cnt = 0 ; ans = 0

for i in range(1, len(string)):
    char = string[i]
    if char == "(":
        stack.append(char)
    else:
        stack.pop()
        if string[i - 1] == "(":
            ans += len(stack)
        else: ans += 1

print(ans)