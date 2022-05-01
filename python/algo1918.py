from collections import deque

expression = deque(list(input()))

keys = ["+", "-", "*" , "/", "(", ")"]
ans = [] ; stack = []

while expression:
    char = expression.popleft()
    if char in keys:
        if char == "(": 
            stack.append(char)
            continue
        elif char == ")":
            while stack[-1] != "(":
                ans.append(stack.pop())
            stack.pop()
        elif char == "*" or char == "/":
            while stack and (stack[-1] == "*" or stack[-1] =="/"):
                ans.append(stack.pop())
        else:
            while stack and stack[-1] != "(":
                ans.append(stack.pop())
        stack.append(char)
    else: ans.append(char)
    
while stack: ans.append(stack.pop())
for a in ans:
    if a =="(" or a == ")": continue
    print(a,end="")

# numStack deque equStack
# ) 만나면 equStack에 다시 수 append
# a + b * c + d * e * (f + g)
# abc*+fg+de**+
# 다음 eq가 우선순위가 다른지
# 같으면
# abcdefg
# +*+**(+)
# *+ (+)**+

# 자신 뒤 항이 우선순위가 높다면,
# 해당 항은 자신이 가장 클때까지 앞으로 간다
