order = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "(": 3,
    ")": 3
}
stack = []
ans = ""

expression = list(input())
idx = 0

while idx < len(expression):
    e = expression[idx]

    if 65 <= ord(e) <= 90:
        ans += str(e)

    else:
        if stack:
            if e == ")": # 괄호를 벗겨내는 작업
                while stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()
            
            # e가 연산자 일 때, stack의 top보다 
            # 1. 우선순위가 낮거나 같다면 ans에 바로 추가해준다.
            # 2. 우선순위가 높다면 stack에 append해줘야 한다(바로 아래에 적혀있음)
            while stack and order[stack[-1]] >= order[e] and stack[-1] != "(":
                ans += stack.pop()

        if e != ")": stack.append(e) # 괄호를 생성하거나 stack top보다 더 높은 연산자가 추가된다.

    idx += 1

while stack:
    c = stack.pop()
    if c == "(" or c == ")": continue
    ans += c

print(ans)