import sys
input = sys.stdin.readline

n = int(input())

expression = input()[:-1] ; idx = 0
alpha = [0 for _ in range(26)]
stack = []

for i in range(n):
    alpha[i] = int(input())

while idx < len(expression):
    if 65 <= ord(expression[idx]) <= 90:
        stack.append(expression[idx])
    else:
        char1 = stack.pop()
        char2 = stack.pop()
        if type(char1) == str: 
            exp1 = alpha[ord(char1) - ord('A')]
        else: exp1 = char1
        
        if type(char2) == str:
            exp2 = alpha[ord(char2) - ord('A')]
        else:
            exp2 = char2

        val = eval(f'{exp2} {expression[idx]} {exp1}')
        stack.append(val)

    idx += 1

print(f'{stack[0]:.2f}')

        


