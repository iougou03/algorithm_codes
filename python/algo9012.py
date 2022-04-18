# n = int(input())
# ans = []

# def chec_vps(s):
#     val = 0

#     for c in list(s):
#         if c == '(': val += 1
#         elif c == ')': val -= 1
        
#         if val < 0: return "NO"
#     if val > 0: return "NO"
#     else: return "YES"

# for _ in range(n):
#     s = input()    
#     ans.append(chec_vps(s))

# [print(a) for a in ans]


import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = list(input())[:-1]
    ans = 0

    for c in string:
        if c == "(": ans += 1
        else: ans -= 1
        
        if ans < 0: 
            break
    
    if ans: print("NO")
    else: print("YES")


