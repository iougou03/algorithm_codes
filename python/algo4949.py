ans = []

def check_balance(s):
    stack = []
    
    for c in list(s):
        if c == "(" or c == ")" or c == "[" or c == "]":
            if not stack: 
                if c == "]" or c == ")": return "no"
                else: stack.append(c)
            else:
                top = stack[-1]
                if c == ")" and top == "(": stack.pop()
                elif c == "]" and top == "[": stack.pop()
                elif c == ")" and top == "[": return "no"
                elif c == "]" and top == "(": return "no"
                else: stack.append(c)
    
    if stack: return "no"
    else: return "yes"

while True:
    s = input()
    if s == ".": break
    ans.append(check_balance(s))

[print(a) for a in ans]